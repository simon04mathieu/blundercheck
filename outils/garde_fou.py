"""Garde-fou de publication (demande de Simon, 23/10/2026) : on ne publie JAMAIS ailleurs que sur les comptes BlunderCheck.

Chaque outil (meta.py, threads.py, tiktok.py, youtube.py) appelle verifier(...) juste avant chaque envoi, avec
l'identité réelle du compte lue auprès du réseau (pas une valeur de configuration). Si le compte n'est pas dans la liste
ci-dessous, l'envoi est refusé (« ÉCHEC : GARDE-FOU ») et rien ne part. Les comptes personnels de Simon (profil Facebook,
Instagram, TikTok, YouTube perso) n'y sont pas et n'y seront jamais.

Seul Simon peut ajouter un compte ici (règle fixe 14 de claude/systeme-agents.md), quand il ouvre un nouveau compte BlunderCheck.
"""
import sys

AUTORISES = {
    # Page Facebook « BlunderCheck » (Page d'entreprise, jamais un profil personnel)
    "facebook": {"BlunderCheck"},
    # Comptes Instagram professionnels BlunderCheck (nom d'utilisateur)
    "instagram": {"blundercheckapp", "blundercheckches"},
    # Profils Threads BlunderCheck (nom d'utilisateur)
    "threads": {"blundercheckapp"},
    # Comptes TikTok BlunderCheck (nom d'utilisateur) : FR et EN
    "tiktok": {"blundercheckapp", "blundercheck.ches"},
    # Chaînes YouTube BlunderCheck (identifiant de chaîne)
    "youtube": {"UCOeNkeulS5bvT5MQ9ZjhqmA"},
}


def verifier(reseau, identite, page=None):
    """Arrête tout si `identite` (nom d'utilisateur, nom de Page ou id de chaîne lu auprès du réseau) n'est pas autorisée.
    Pour Facebook, `page` = True seulement si le réseau a confirmé que la cible est une Page (et non un profil)."""
    ok = reseau in AUTORISES and str(identite or "").strip().lstrip("@") in AUTORISES[reseau]
    if reseau == "facebook" and page is not True:
        ok = False
    if not ok:
        sys.exit(f"ÉCHEC : GARDE-FOU {reseau} : compte « {identite} » hors de la liste des comptes BlunderCheck autorisés "
                 f"(outils/garde_fou.py). Rien n'a été publié.")
    return True
