"""Diagnostic des tâches GitHub Actions : à lancer AU LIEU d'attendre quand quelque chose semble long.

    python3 outils/diagnostic.py            # toutes les tâches récentes
    python3 outils/diagnostic.py --annuler  # annule aussi les tâches clairement bloquées (à relancer ensuite)

Pour chaque tâche en cours ou récente : l'étape où elle se trouve, depuis combien de temps,
la durée normale de cette étape (moyenne des dernières réussites), et un verdict en clair.
Pour une tâche échouée : l'étape fautive et les dernières lignes d'erreur.
Besoin : le CLI `gh` connecté (présent dans les sessions Claude et sur GitHub Actions).
"""
import datetime as dt, json, re, subprocess, sys

DEPOT = "simon04mathieu/blundercheck"
# au-delà de NORMAL x FACTEUR (et au moins MIN_BLOQUE minutes), une étape est considérée bloquée
FACTEUR, MIN_BLOQUE = 3.0, 6.0
# file d'attente : au-delà, c'est GitHub qui n'a pas de machine libre (rien à corriger chez nous)
MAX_FILE = 10.0
CAUSES = [  # motif dans le nom d'étape ou le journal -> explication en clair
    (r"apt-get|Outils|pip install", "installation des outils : serveur de paquets lent ou en panne chez GitHub/Ubuntu. Annuler et relancer."),
    (r"ElevenLabs .* -> 401|quota_exceeded|insufficient", "ElevenLabs : clé refusée ou crédits épuisés."),
    (r"ElevenLabs .* -> 429", "ElevenLabs : trop de demandes à la fois. Relancer plus tard."),
    (r"YouTube|googleapis.*40[13]", "YouTube : autorisation expirée ou refusée (jeton à renouveler)."),
    (r"unaudited_client|tiktokapis.*40[13]", "TikTok : publication refusée (appli non auditée, ou jeton expiré)."),
    (r"faster_whisper|WhisperModel", "transcription de la voix (Whisper) : téléchargement du modèle lent ou en échec."),
    (r"ffmpeg", "montage vidéo (ffmpeg) : fichier manquant ou commande en erreur."),
    (r"push|rejected|non-fast-forward", "dépôt GitHub : envoi refusé (quelqu'un a poussé en même temps). Relancer."),
    (r"Traceback|Error|SystemExit", "erreur Python dans nos outils : voir les dernières lignes."),
]

def gh(*args):
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    if r.returncode: raise SystemExit(f"gh {' '.join(args[:3])}… : {r.stderr.strip()[:300]}")
    return r.stdout

def api(chemin): return json.loads(gh("api", chemin))

def t(s): return dt.datetime.fromisoformat(s.replace("Z", "+00:00")) if s else None

def minutes(a, b): return (b - a).total_seconds() / 60 if a and b else 0.0

def cause(texte):
    return next((c for m, c in CAUSES if re.search(m, texte or "", re.I)), None)

def normales(workflow_id):
    """Durée moyenne de chaque étape sur les 5 dernières réussites de ce workflow."""
    runs = api(f"repos/{DEPOT}/actions/workflows/{workflow_id}/runs?status=success&per_page=5")["workflow_runs"]
    tot = {}
    for r in runs:
        for j in api(f"repos/{DEPOT}/actions/runs/{r['id']}/jobs")["jobs"]:
            for s in j["steps"]:
                if s.get("started_at") and s.get("completed_at"):
                    tot.setdefault(s["name"], []).append(minutes(t(s["started_at"]), t(s["completed_at"])))
    return {k: sum(v) / len(v) for k, v in tot.items()}

def journal_echec(run_id):
    try:
        lignes = gh("run", "view", str(run_id), "-R", DEPOT, "--log-failed").splitlines()
    except SystemExit:
        return ""
    return "\n".join(l.split("\t")[-1][-200:] for l in lignes[-15:])

def main(annuler=False):
    maintenant = dt.datetime.now(dt.timezone.utc)
    runs = api(f"repos/{DEPOT}/actions/runs?per_page=15")["workflow_runs"]
    vus, bloques, rapport = set(), [], []
    cache_normales = {}
    for r in runs:
        if r["status"] == "completed":
            # seule la tâche terminée la plus récente de chaque workflow compte : un échec suivi d'une réussite est réglé
            if r["workflow_id"] in vus: continue
            vus.add(r["workflow_id"])
            if r["conclusion"] in ("success", "skipped", "cancelled", "neutral"): continue
        titre = f"{r['name']} « {r['display_title'][:50]} » (#{r['id']})"
        debut = t(r.get("run_started_at") or r["created_at"])
        if r["status"] in ("queued", "pending", "waiting", "requested"):
            m = minutes(t(r["created_at"]), maintenant)
            v = "normal" if m < MAX_FILE else "GitHub n'a pas de machine libre (panne ou file chargée chez GitHub, rien à corriger chez nous)"
            rapport.append(f"⏳ {titre} : en file depuis {m:.0f} min → {v}")
            continue
        jobs = api(f"repos/{DEPOT}/actions/runs/{r['id']}/jobs")["jobs"]
        if r["status"] == "in_progress":
            if r["workflow_id"] not in cache_normales:
                cache_normales[r["workflow_id"]] = normales(r["workflow_id"])
            norm = cache_normales[r["workflow_id"]]
            for j in jobs:
                for s in j["steps"]:
                    if s["status"] != "in_progress": continue
                    m = minutes(t(s.get("started_at")), maintenant); n = norm.get(s["name"])
                    limite = max(MIN_BLOQUE, (n or 0) * FACTEUR)
                    if m > limite:
                        c = cause(s["name"]) or "étape anormalement longue"
                        rapport.append(f"🔴 {titre} : BLOQUÉE à l'étape « {s['name']} » depuis {m:.0f} min "
                                       f"(normale : {n:.1f} min)" if n else
                                       f"🔴 {titre} : BLOQUÉE à l'étape « {s['name']} » depuis {m:.0f} min (pas de référence)")
                        rapport.append(f"   cause probable : {c}")
                        bloques.append(r["id"])
                    else:
                        rapport.append(f"🟢 {titre} : étape « {s['name']} » depuis {m:.1f} min"
                                       + (f" (normale : {n:.1f} min)" if n else "") + " → ça avance")
            continue
        # échec
        etape = next((s["name"] for j in jobs for s in j["steps"] if s.get("conclusion") == "failure"), "?")
        log = journal_echec(r["id"])
        rapport.append(f"❌ {titre} : ÉCHEC à l'étape « {etape} » ({minutes(debut, t(r['updated_at'])):.0f} min, {r['updated_at'][:16]}Z)")
        rapport.append(f"   cause probable : {cause(etape + chr(10) + log) or 'voir les lignes ci-dessous'}")
        if log: rapport += ["   | " + l for l in log.splitlines()[-8:]]
    if not rapport:
        rapport = ["✅ Rien d'anormal : aucune tâche en cours, en file ou en échec récent."]
    print("\n".join(rapport))
    if annuler and bloques:
        for i in bloques:
            gh("run", "cancel", str(i), "-R", DEPOT); print(f"→ tâche #{i} annulée : la relancer (gh run rerun {i} -R {DEPOT})")

if __name__ == "__main__":
    main("--annuler" in sys.argv)
