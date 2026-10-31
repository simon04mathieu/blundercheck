# Pièges candidats (réserve du Scénariste)

*Généré le 31/10/2026 par `outils/chercher_pieges.py` (puzzles Lichess, CC0) : pièges d'ouverture à mat où de vrais joueurs
tombent souvent (puzzle classé 1300-2000, mat en 2 à 4 **ou gain d'une pièce** en 2 à 4 coups). Ligne vérifiée python-chess + Stockfish 1 s. « Déjà fait » = d'après `marketing/deja-fait.md`.
**Variété (Simon, 31/10)** : au plus 1 piège par motif + pièce finale, au plus 3 sacrifices de dame ; le Scénariste ne répète pas le motif ni la pièce qui mate de la veille.
Le Scénariste prend d'abord les « non » ; « fr » seul = jumeau EN possible, et inversement.*

| # | Ouverture | Parties réelles | Note moy. | Type | Motif | Pièce finale | Sac. dame | Héros | Gaffe (coup juste) | Ligne | Déjà fait |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Sicilian Defense Accelerated Dragon | 4 | 1693 | gain | trappedPiece | gain | non | blancs | d5?? (Nxe4) | `e4 c5 Nc3 Nc6 Nf3 g6 d4 cxd4 Nxd4 Bg7 Be3 Nf6 Bc4 Qb6 Nb3 Qb4 Bd3 d5 Bc5 Qxc3+ bxc3` | non |
| 2 | Ruy Lopez Schliemann Defense | 4 | 1918 | gain | attraction | gain | non | noirs | Nc4?? (Bxf6) | `e4 e5 Nf3 Nc6 Bb5 f5 O-O fxe4 Bxc6 dxc6 Nxe5 Nf6 d4 Bd6 Bg5 O-O Nc3 Qe8 Nc4 Bxh2+ Kxh2 Ng4+ Kg1 Qh5` | non |
| 3 | Russian Game Other variations | 3 | 1307 | gain | fork | gain | non | blancs | c5?? (d5) | `e4 e5 Nf3 Nf6 Nxe5 d6 Nf3 Nxe4 c3 c5 Qa4+ Nc6 Qxe4+` | non |
| 4 | Scandinavian Defense Main Line | 3 | 1646 | gain | clearance | gain | non | blancs | Qa4?? (c5) | `e4 d5 exd5 Qxd5 Nc3 Qa5 b4 Qxb4 Nb5 Na6 Ba3 Qa5 Qh5 Qa4 Nd6+ exd6 Bb5+` | non |
| 5 | Alekhine Defense Modern Variation | 3 | 1689 | mat en 2 | sacrifice | pion | oui | blancs | h6?? (Qe8) | `e4 Nf6 e5 Nd5 d4 d6 Nf3 Bf5 Bc4 Nb6 Bxf7+ Kxf7 Ng5+ Kg8 e6 Bg6 Qf3 h6 Qf7+ Bxf7 exf7#` | en |
| 6 | Englund Gambit Complex Englund Gambit | 3 | 1352 | mat en 2 | smotheredMate | cavalier | oui | noirs | Nb5?? (h3) | `d4 Nc6 Nf3 e5 dxe5 Qe7 e4 Nxe5 Nxe5 Qxe5 Bd3 Bc5 O-O Nf6 Kh1 d6 f4 Qd4 Nc3 Ng4 Nb5 Qg1+ Rxg1 Nf2#` | non |
| 7 | Indian Defense Other variations | 2 | 1716 | gain | discoveredAttack | gain | non | blancs | e5?? (h6) | `d4 Nf6 Nc3 g6 e4 Bg7 Bg5 d6 Qd2 e5 dxe5 dxe5 Qxd8+` | non |
| 8 | Queens Pawn Game Krause Variation | 2 | 1385 | mat en 2 | autre | dame | non | noirs | Bxf6?? (Qe2) | `d4 d5 Nf3 c5 dxc5 e6 Bg5 Nf6 e4 Bxc5 exd5 Qb6 Bxf6 Bxf2+ Kd2 Qe3#` | non |
