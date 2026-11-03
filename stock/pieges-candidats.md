# Pièges candidats (réserve du Scénariste)

*Généré le 03/11/2026 par `outils/chercher_pieges.py` (puzzles Lichess, CC0) : pièges d'ouverture à mat où de vrais joueurs
tombent souvent (puzzle classé 1000-2000, idéal ≈ 1550 ; mat en 2 à 5 **ou gain d'une pièce** en 2 à 5 coups ; réserve cumulée, jamais écrasée). Ligne vérifiée python-chess + Stockfish 1 s. « Déjà fait » = d'après `marketing/deja-fait.md`.
**Variété (Simon, 31/10)** : au plus 1 piège par motif + pièce finale, au plus 1 sacrifice de dame par recherche (Simon, 3/11) ; le Scénariste ne répète pas le motif ni la pièce qui mate de la veille.
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
| 9 | Sicilian Defense Open (piège composé par le Producteur, 3/11) | composé | — | gain | intermezzo (échec intermédiaire) | gain | non | blancs | Nxe4?? (g6 / a6 (Najdorf, Dragon)) | `e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 Nxe4 Nxe4 d5 Bb5+ Bd7 Bxd7+ Nxd7 Ng3` | non |
| 10 | Sicilian Defense Marshall Gambit | 4 | 1493 | gain | clearance | gain | non | blancs | O-O?? (Bd7) | `fen:r1bqk2r/1p2nppp/p1n1p3/2bpP3/8/2NB1N2/PPP2PPP/R1BQ1RK1_b_kq_-_3_8 O-O Bxh7+ Kxh7 Ng5+ Kg8 Qh5` | non |
| 11 | Scotch Game Other variations | 4 | 1401 | gain | discoveredAttack | gain | non | noirs | O-O?? (Bxf6) | `fen:r1bqk2r/pp2bppp/3p1n2/3Bp1B1/4P3/5N2/PPP2PPP/R2QK2R_w_KQkq_-_1_10 O-O Nxd5 Qxd5 Bxg5 Nxg5 Qxg5` | non |
| 12 | Sicilian Defense Old Sicilian | 4 | 1776 | gain | pin | gain | oui | blancs | Nfd7?? (Bd7) | `fen:r2qkb1r/pp2pppp/3p1n2/1Bp1n3/4P1b1/2P2N2/PP1P1PPP/RNBQR1K1_b_kq_-_2_7 Nfd7 Nxe5 Bxd1 Bxd7+ Qxd7 Nxd7` | non |
| 13 | Ruy Lopez Schliemann Defense | 4 | 1917 | gain | attraction | gain | non | noirs | Nc4?? (Bxf6) | `fen:r1b1qrk1/ppp3pp/2pb1n2/4N1B1/3Pp3/2N5/PPP2PPP/R2Q1RK1_w_-_-_5_10 Nc4 Bxh2+ Kxh2 Ng4+ Kg1 Qh5` | en |
| 14 | Sicilian Defense Smith-Morra Gambit | 3 | 1534 | gain | fork | gain | non | blancs | a6?? (e5) | `fen:r1bqkbnr/pp1p1ppp/2n1p3/1N6/4PB2/8/PP3PPP/R2QKBNR_b_KQkq_-_3_6 a6 Nc7+ Qxc7 Bxc7 Bb4+ Ke2` | non |
| 15 | Horwitz Defense Other variations | 3 | 1279 | gain | trappedPiece | gain | non | blancs | f6?? (Be7) | `fen:rn1qk1nr/pbpp1ppp/1p1bp3/4N3/3P1B2/4P3/PPP2PPP/RN1QKB1R_b_KQkq_-_2_5 f6 Qh5+ g6 Nxg6 hxg6 Qxh8` | non |
| 16 | Petrovs Defense Damiano Variation | 3 | 1841 | mat en 3 | sacrifice | dame | non | noirs | Kh1?? (Rf2) | `fen:rnb1k2r/ppp2ppp/5q2/2bpN3/4nP2/3B4/PPPP2PP/RNBQ1RK1_w_kq_-_1_7 Kh1 Ng3+ hxg3 Qh6+ Qh5 Qxh5#` | non |
| 17 | Nimzo-Indian Defense Leningrad Variation | 3 | 1052 | gain | deflection | gain | non | noirs | Bxf6?? (Bd2) | `fen:rnb1k2r/pp1p1ppp/4pn2/q5B1/1bPN4/2N5/PP2PPPP/R2QKB1R_w_KQkq_-_1_7 Bxf6 Bxc3+ bxc3 Qxc3+ Qd2 Qxa1+` | non |
| 18 | Queens Gambit Declined Albin Countergambit | 2 | 1642 | mat en 3 | autre | dame | non | noirs | h3?? (Nb3) | `fen:r2qk2r/ppp1bppp/2n4n/4P3/1PPp1Pb1/P4N2/3NP1PP/R1BQKB1R_w_KQkq_-_1_9 h3 Bh4+ Nxh4 Qxh4+ g3 Qxg3#` | non |
| 19 | Vienna Game Stanley Variation | 2 | 1741 | mat en 3 | deflection | dame | non | noirs | Qxh8?? (c3) | `fen:r1b1k1nr/pppp1pQ1/8/2bNp2p/2BnP2q/7N/PPPP2PP/R1BK3R_w_kq_-_3_9 Qxh8 Qg4+ Ke1 Nxc2+ Kf1 Qd1#` | non |
| 20 | Bishops Opening Other variations | 2 | 1874 | mat en 3 | enPassant | dame | non | blancs | Kg8?? (Ke8) | `fen:r1bq1b1r/pppp1kpp/2n5/4P1N1/6n1/2Pp4/PP3PPP/RNBQK2R_b_KQ_-_2_8 Kg8 Qb3+ d5 exd6+ Be6 Qxe6#` | non |
