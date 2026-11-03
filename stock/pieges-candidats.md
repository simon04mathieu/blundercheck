# Pièges candidats (réserve du Scénariste)

*Réécrit le 3/11 vers 2 h par le Producteur, sur ordre de Simon (« s'il reste 0 piège, invente-en 1, supprime le reste »). L'ancienne réserve (8 lignes, toutes faites, en double ou sacrifices de dame) est supprimée ; la recherche Lichess du 3/11 avait trouvé 0 piège. Le piège ci-dessous est **composé** (pas tiré d'un puzzle) : ne jamais dire « X real games ». Ligne vérifiée python-chess + Stockfish 16 (profondeur 22) ; anti-doublon `deja_fait.py` : NOUVEAU (FR et EN).*

| # | Ouverture | Parties réelles | Note moy. | Type | Motif | Pièce finale | Sac. dame | Héros | Gaffe (coup juste) | Ligne | Déjà fait |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Sicilienne ouverte (composé) | — (composé) | niveau visé 1300-1700 | gain | échec intermédiaire Fb5+ | gain d'une pièce | non | blancs | 5…Cxe4?? (5…g6 ou 5…a6) | `e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 Nxe4 Nxe4 d5 Bb5+ Bd7 Bxd7+ Nxd7 Ng3` | non |

**Idée** : les Noirs prennent le pion central avec le cavalier en comptant sur le « truc du pion » (6.Cxe4 d5, le pion attaque le cavalier et récupère la pièce). Mais 7.Fb5+ ! : l'échec passe avant ; après 7…Fd7 8.Fxd7+ Cxd7, le cavalier se retire (9.Cg3) et les Blancs gardent une pièce de plus (Stockfish +394 centipions). 6…Da5+ ne sauve rien non plus : 7.Cc3 (+4,8).
