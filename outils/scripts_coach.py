"""Textes des vidéos coach. Repères entre crochets, placés juste avant le mot où l'action doit tomber :
[m SAN badge?]  joue un coup (badge : livre, bizarre, erreur, gaffe, mat, meilleur, bon)
[f a1b2 c3d4]   flèches
[p SAN SAN ...] remet la position (coups depuis le départ)
"""
SCRIPTS = {
"blackburne": ("blancs", """[m e4 livre] Après e4 [m e5 livre] e5, [m Nf3 livre] cavalier f3, [m Nc6 livre] cavalier c6, tu joues [m Bc4 livre] fou c4 ?
C'est l'Italienne, l'ouverture préférée des débutants. Mais fais très attention à ce coup : [m Nd4 bizarre] cavalier d4.
Ça ressemble à une erreur. Le pion e5 n'est plus défendu, [f f3e5] et ton cavalier peut le prendre.
Beaucoup de joueurs le prennent. [m Nxe5 erreur] Erreur. La dame noire sort en [m Qg5] g5.
Regarde : elle attaque [f g5e5 g5g2] ton cavalier, et ton pion g2.
Si tu continues avec [m Nxf7 gaffe] cavalier prend f7, pour attaquer la tour, c'est fini.
Dame prend [m Qxg2] g2. Tour [m Rf1] f1. Dame prend [m Qxe4+] e4, échec. Fou [m Be2] e2, et cavalier [m Nf3# mat] f3.
Échec et mat. Le bon coup, c'était simplement [p e4 e5 Nf3 Nc6 Bc4 Nd4] [f f3d4] cavalier prend [m Nxd4 meilleur] d4.
Tu échanges le cavalier gênant, et c'est toi qui es mieux.
Tu veux savoir quelles erreurs te coûtent tes parties ? Analyse-les gratuitement sur BlunderCheck."""),

"berger": ("noirs", """Tu joues les Noirs. Après e4 [m e4] [m e5 livre] e5, ton adversaire sort son fou en [m Bc4 livre] c4.
Tu joues [m Nc6 livre] cavalier c6, normal. Et là, la dame sort en [m Qh5 bizarre] h5.
C'est le coup du berger : la dame et le fou visent tous les deux [f h5f7 c4f7] le pion f7.
Et ce pion n'est défendu que par ton roi.
Le réflexe de beaucoup de joueurs, c'est d'attaquer la dame avec [m Nf6 gaffe] cavalier f6. Erreur fatale.
Dame prend [m Qxf7# mat] f7, et c'est mat en quatre coups. Ton roi ne peut pas reprendre, parce que le fou protège la dame.
Alors, comment se défendre ? [p e4 e5 Bc4 Nc6 Qh5] Il faut d'abord fermer la route de la dame avec [m g6 meilleur] g6.
La dame doit reculer, souvent en [m Qf3] f3, pour viser f7 encore une fois.
Et maintenant seulement, [m Nf6 bon] cavalier f6 : la route vers f7 est bloquée, et tu es même un peu mieux.
Tu veux savoir quelles erreurs te coûtent tes parties ? Analyse-les gratuitement sur BlunderCheck."""),

"petrov": ("noirs", """Tu joues la défense russe avec les Noirs : [m e4] e4 [m e5 livre] e5, [m Nf3] cavalier f3, [m Nf6 livre] cavalier f6.
Les Blancs prennent ton pion [m Nxe5] e5. Le réflexe, c'est de copier : cavalier prend [m Nxe4] e4.
Attention, ici la copie s'arrête. Dame [m Qe2] e2 ! La dame attaque ton cavalier [f e2e4] en e4.
Beaucoup de joueurs reculent avec [m Nf6 gaffe] cavalier f6. Et là, catastrophe.
Cavalier c6, [m Nc6+ bon] échec à la découverte ! La dame donne échec sur la colonne e,
et en même temps, le cavalier attaque [f c6d8] ta dame en d8.
Tu dois parer l'échec, [m Qe7] et tu perds ta [m Nxe7] dame.
Le bon coup, c'était [p e4 e5 Nf3 Nf6 Nxe5 Nxe4 Qe2] dame [m Qe7 meilleur] e7. Tu bloques la colonne e.
Les Blancs reprennent ton cavalier, puis d6 attaque le cavalier cloué, et tu récupères ta pièce.
Retiens : dans la défense russe, on joue d'abord d6, avant de reprendre en e4.
Analyse tes parties gratuitement sur BlunderCheck."""),

"damiano": ("noirs", """Après e4 [m e4] [m e5 livre] e5, cavalier [m Nf3] f3, ton pion e5 est attaqué.
Beaucoup de débutants le défendent avec [m f6 erreur] f6. Mauvaise idée, et je vais te montrer pourquoi.
Les Blancs sacrifient leur cavalier : cavalier prend [m Nxe5 bon] e5 !
Si tu reprends avec f prend [m fxe5 gaffe] e5, la dame arrive en [m Qh5+] h5, échec.
Ton pion f6 a ouvert la diagonale [f h5e8] de ton roi.
Tu bloques avec [m g6] g6, et la dame prend [m Qxe5+] e5, échec, et elle attaque [f e5h8] ta tour h8 en même temps.
Tu pares l'échec, [m Qe7] et ta tour [m Qxh8] tombe.
Le bon coup, c'était [p e4 e5 Nf3 f6 Nxe5] dame [m Qe7 meilleur] e7. Tu ne prends pas le cavalier, tu l'attaques avec ta dame.
Tu restes moins bien, mais tu évites le désastre.
Et la vraie leçon : pour défendre e5, joue cavalier c6, pas f6.
Analyse tes parties gratuitement sur BlunderCheck."""),

"carokann": ("noirs", """Tu joues la Caro-Kann : e4 [m e4] [m c6 livre] c6, d4 [m d4] [m d5 livre] d5, cavalier [m Nc3] c3, d prend [m dxe4] e4, cavalier prend [m Nxe4] e4.
Tu développes ton cavalier en [m Nd7 livre] d7. Les Blancs jouent dame [m Qe2 bizarre] e2.
Ça a l'air d'un coup bizarre, mais regarde : la dame est sur la même colonne [f e2e8] que ton roi.
Ton pion e7 est cloué. Si tu sors l'autre cavalier en f6, [m Ngf6 gaffe] sans réfléchir,
c'est cavalier [m Nd6# mat] d6, échec et mat ! Le pion e7 ne peut pas prendre : il est cloué.
Et ton roi n'a aucune case : ton propre cavalier en d7 lui bloque la sortie.
Le bon coup, c'était [p e4 c6 d4 d5 Nc3 dxe4 Nxe4 Nd7 Qe2] le cavalier de d7 en [m Ndf6 meilleur] f6.
Le même coup, mais avec l'autre cavalier : la case d7 se libère, et ton roi peut respirer.
Analyse tes parties gratuitement sur BlunderCheck."""),

"canne": ("blancs", """Tu joues l'Espagnole avec les Blancs : e4 [m e4 livre] [m e5 livre] e5, cavalier [m Nf3 livre] f3, cavalier [m Nc6 livre] c6, fou [m Bb5 livre] b5.
Les Noirs jouent [m Nf6 livre] cavalier f6, tu [m O-O livre] roques. Et là, coup bizarre : cavalier [m Ng4 bizarre] g4.
Tu le chasses avec [m h3] h3, et au lieu de reculer, les Noirs jouent [m h5 bizarre] h5 !
Le cavalier reste en prise. C'est un appât.
Si tu le prends, [m hxg4 gaffe] h prend g4, [m hxg4] la colonne h s'ouvre vers ton roi. [f h8h1]
Ton cavalier [m Ne1] recule, la dame arrive en [m Qh4] h4, tu joues [m f3] f3, pion [m g3] g3,
et rien n'arrête la dame : [m Bxc6] dame [m Qh1# mat] h1, échec et mat.
Le bon réflexe : ne mords pas à l'hameçon. [p e4 e5 Nf3 Nc6 Bb5 Nf6 O-O Ng4 h3 h5] Joue [m c3 meilleur] c3,
et ce cavalier en g4 est juste mal placé : c'est toi qui es mieux.
Analyse tes parties gratuitement sur BlunderCheck."""),

"magnus": ("noirs", """Tu joues la Sicilienne avec les Noirs. e4 [m e4] [m c5 livre] c5, cavalier [m Nf3] f3, [m d6 livre] d6,
d4, [m d4] c prend [m cxd4] d4, cavalier prend [m Nxd4] d4, cavalier [m Nf6 livre] f6, cavalier [m Nc3] c3, cavalier [m Nc6 livre] c6.
Les Blancs sortent leur fou en [m Bc4] c4, tu joues [m g6] g6.
Échange en [m Nxc6] c6, b prend [m bxc6] c6. Et là, pion [m e5 bon] e5 ! Il attaque [f e5f6] ton cavalier f6.
Le réflexe, c'est de prendre : d prend [m dxe5 gaffe] e5. Grave erreur.
Fou prend [m Bxf7+ bon] f7, échec ! Ton roi doit [m Kxf7] reprendre,
et la colonne d est ouverte : [f d1d8] dame prend [m Qxd8] d8. Ta dame tombe.
Le bon coup, c'était [p e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 Nc6 Bc4 g6 Nxc6 bxc6 e5] cavalier [m Ng4 meilleur] g4.
Tu sauves ton cavalier, ta dame reste protégée, et la partie reste jouable.
Analyse tes parties gratuitement sur BlunderCheck."""),

"elephant": ("blancs", """Tu joues le gambit dame avec les Blancs : d4 [m d4 livre] [m d5 livre] d5, c4 [m c4 livre] [m e6 livre] e6, cavalier [m Nc3 livre] c3, cavalier [m Nf6 livre] f6, fou [m Bg5 livre] g5.
Les Noirs jouent [m Nbd7] cavalier d7. Tu échanges en [m cxd5] d5, [m exd5] e prend d5,
et le pion d5 a l'air gratuit : ton cavalier peut [f c3d5] le prendre.
Ne le prends pas ! C'est le piège de l'éléphant.
Si tu prends, [m Nxd5 gaffe] les Noirs reprennent avec leur cavalier [m Nxd5 bizarre] et te laissent leur dame.
Tu la prends, [m Bxd8] et fou b4, [m Bb4+ bon] échec !
Ta dame doit s'interposer, [m Qd2] fou prend [m Bxd2+] d2, roi prend [m Kxd2] d2, roi prend [m Kxd8] d8.
Résultat : tu as perdu une pièce entière.
Le bon coup, c'était [p d4 d5 c4 e6 Nc3 Nf6 Bg5 Nbd7 cxd5 exd5] [m e3 meilleur] e3. Tranquille, solide, et la partie est égale.
Analyse tes parties gratuitement sur BlunderCheck."""),
}

import re
def texte_voix(s):
    t = re.sub(r"\[[^\]]*\]", "", s)
    return re.sub(r"\s+", " ", t).strip()

# ---------- lot 2 : quiz, légendes, rafales (21/10) ----------
F_TOUR = "fen:r1bqk2r/ppppbpp1/2n2n2/4p3/2B1P3/5N2/PPPP1PP1/RNBQK2R_w_KQkq_-_0_6"
F_CASE = "fen:r1bqk1nr/pppp1ppp/2n5/4p3/2b1P3/5N2/PPP2PPP/RNBQK2R_w_KQkq_-_0_6"
F_ROIS = "fen:8/8/4k3/8/4K3/8/8/8_w_-_-_0_1"
F_DAMES = "fen:6k1/1P3ppp/8/8/8/8/5PPP/3Q2K1_w_-_-_0_1"
OPERA = "e4 e5 Nf3 d6 d4 Bg4 dxe5 Bxf3 Qxf3 dxe5 Bc4 Nf6 Qb3 Qe7 Nc3 c6 Bg5 b5"
IMM = "e4 e5 f4 exf4 Bc4 Qh4+ Kf1 b5 Bxb5 Nf6 Nf3 Qh6 d3 Nh5 Nh4 Qg5 Nf5 c6 g4 Nf6 Rg1 cxb5"
SCRIPTS.update({
"enpassant": ("blancs", """Ce pion va prendre… dans le vide. Et pourtant, c'est un coup légal. Regarde. [m e4] e4, cavalier [m Nf6] f6.
Le pion avance en [m e5] e5 et chasse le cavalier. Les Noirs jouent [m d5] d5 : leur pion avance de deux cases, [f d7d5] et arrive juste à côté du pion blanc.
Et là, le pion blanc prend [m exd6 bon] en d6, sur une case vide. Le pion d5 disparaît.
C'est la prise en passant. Quand un pion avance de deux cases et arrive à côté d'un pion adverse, celui-ci peut le prendre comme s'il n'avait avancé que d'une case.
Une seule condition : il faut le faire tout de suite, au coup suivant. Si tu attends, c'est trop tard.
Beaucoup de joueurs croient à un bug quand ça leur arrive en ligne. Maintenant, tu sais.
Analyse tes parties gratuitement sur BlunderCheck."""),

"tour_attaquee": ("blancs", f"""[p {F_TOUR}] Les Blancs veulent roquer. Mais regarde : la tour h1 est attaquée [f h8h1] par la tour noire.
Est-ce qu'ils ont le droit de roquer ? Réfléchis deux secondes…
La réponse : oui ! [m O-O bon] Le roque est légal.
Pour roquer, il y a trois conditions, et elles concernent toutes le roi.
Un : le roi ne doit pas être en échec. Deux : il ne doit pas traverser une case attaquée. Trois : il ne doit pas arriver sur une case attaquée.
Ici, le roi passe par f1 et arrive en g1, deux cases que personne n'attaque. La tour, elle, a le droit d'être attaquée.
Beaucoup de joueurs n'osent pas roquer dans cette situation, alors qu'ils pourraient.
Analyse tes parties gratuitement sur BlunderCheck."""),

"case_attaquee": ("blancs", f"""[p {F_CASE}] Les Blancs veulent roquer. Le roi n'est pas en échec, il n'a jamais bougé, la tour non plus.
Alors, le roque est permis ? Réfléchis…
La réponse : non, c'est interdit ! Regarde le fou noir en c4. [f c4f1] Il contrôle la case f1.
Et pour roquer, le roi doit passer par f1. [f e1g1 c4f1] Or le roi n'a jamais le droit de traverser une case attaquée.
Même s'il n'est pas en échec au départ, et même s'il n'est pas en échec à l'arrivée.
La bonne idée, c'est de bloquer la diagonale du fou. Par exemple, dame [m Qe2 meilleur] e2.
La case f1 n'est plus attaquée, et le roque redevient possible.
Analyse tes parties gratuitement sur BlunderCheck."""),

"rois": ("blancs", f"""[p {F_ROIS}] Le roi blanc veut avancer en e5, [f e4e5] pour se rapprocher du roi noir.
Est-ce que c'est permis ? Réfléchis…
Non ! C'est interdit. La case e5 touche le roi noir : [f e6e5] elle est attaquée par lui.
Et un roi n'a jamais le droit d'aller sur une case attaquée.
Donc deux rois ne peuvent jamais se toucher. Il reste toujours au moins une case entre eux.
C'est ce qu'on appelle l'opposition, et en finale, elle décide souvent de la partie : le roi qui doit jouer est obligé de céder le passage.
Ici, les Blancs peuvent jouer roi [m Kd4 bon] d4, ou f4, mais jamais e5.
Analyse tes parties gratuitement sur BlunderCheck."""),

"deux_dames": ("blancs", f"""[p {F_DAMES}] Les Blancs ont déjà une dame. Et leur pion b7 arrive au bout de l'échiquier.
Est-ce qu'il a le droit de devenir une deuxième dame ? Réfléchis…
Oui ! Pion b8, [m b8=Q# mat] dame. Et en plus, c'est échec et mat !
La nouvelle dame attaque le roi sur la dernière rangée, [f b8g8] et ses propres pions l'empêchent de fuir.
La règle est simple : quand un pion arrive au bout, il se transforme en la pièce de ton choix. Dame, tour, fou ou cavalier, mais jamais un roi.
Et ça ne dépend pas des pièces que tu as déjà. En théorie, tu peux avoir jusqu'à neuf dames en même temps.
Analyse tes parties gratuitement sur BlunderCheck."""),

"opera": ("blancs", f"""Paris, 1858. Paul Morphy joue contre deux nobles, pendant un opéra. Il va gagner en dix-sept coups.
[p {OPERA}] Après neuf coups, Morphy a sorti toutes ses pièces. Les Noirs, eux, n'ont presque rien développé.
Alors il frappe : cavalier prend [m Nxb5 bon] b5 ! [m cxb5] Les Noirs prennent. Fou prend [m Bxb5+] b5, échec. [m Nbd7] Cavalier d7.
[m O-O-O] Grand roque, [m Rd8] tour d8. Tour prend [m Rxd7 bon] d7 ! Encore un sacrifice.
[m Rxd7] Tour prend, [m Rd1] l'autre tour arrive. [m Qe6] Dame e6. Fou prend [m Bxd7+] d7, échec, [m Nxd7] cavalier prend.
Et maintenant, dame [m Qb8+ meilleur] b8, échec ! Il donne sa dame. [m Nxb8] Le cavalier la prend, et tour [m Rd8# mat] d8. Échec et mat.
Tu veux savoir si tu développes tes pièces assez vite ? Analyse tes parties gratuitement sur BlunderCheck."""),

"reti": ("blancs", """Vienne, 1910. Réti contre Tartakower, un grand maître. La partie va durer onze coups.
[m e4] e4, [m c6] c6, [m d4] d4, [m d5] d5, cavalier [m Nc3] c3, d prend [m dxe4] e4, cavalier prend [m Nxe4] e4, cavalier [m Nf6] f6.
Dame [m Qd3] d3, [m e5] e5. d prend [m dxe5] e5, dame [m Qa5+] a5, échec, fou [m Bd2] d2, dame prend [m Qxe5] e5.
Et là, Réti fait le grand roque, [m O-O-O bizarre] et laisse son cavalier e4 en prise.
Les Noirs le prennent. [m Nxe4 erreur] Erreur. Dame [m Qd8+ meilleur] d8, échec ! Il sacrifie sa dame. Le roi doit [m Kxd8] la prendre.
Fou [m Bg5+ bon] g5 : échec double, du fou et de la tour. [f g5d8 d1d8] Le roi fuit en [m Kc7] c7.
Et fou [m Bd8# mat] d8. Échec et mat, en onze coups.
Tu veux voir les coups que tu rates dans tes parties ? Analyse-les gratuitement sur BlunderCheck."""),

"lasker": ("blancs", """Londres, 1912. Edward Lasker contre George Thomas. Un roi va traverser tout l'échiquier… pour mourir.
[p d4 e6 Nf3 f5 Nc3 Nf6 Bg5 Be7 Bxf6 Bxf6 e4 fxe4 Nxe4 b6 Ne5 O-O Bd3 Bb7] Après neuf coups, tout a l'air calme.
Dame [m Qh5 bizarre] h5, [m Qe7] dame e7. Et là : dame prend [m Qxh7+ meilleur] h7, échec ! Il sacrifie sa dame. [m Kxh7] Le roi prend.
Cavalier prend [m Nxf6+] f6, échec double. [m Kh6] Le roi monte en h6. Cavalier [m Neg4+] g4, échec, [m Kg5] le roi avance.
[m h4+] h4, échec, [m Kf4] f4. [m g3+] g3, échec, [m Kf3] f3. Fou [m Be2+] e2, échec, [m Kg2] g2. Tour [m Rh2+] h2, échec, [m Kg1] g1.
Le roi est parti de g8. Il est arrivé en g1. Et le mat, c'est un coup de roi : [m Kd2# mat] roi d2. La tour a1 donne échec, à la découverte.
Tu veux savoir quelles erreurs te coûtent tes parties ? Analyse-les gratuitement sur BlunderCheck."""),

"immortelle": ("blancs", f"""Londres, 1851. Anderssen contre Kieseritzky. Une partie qu'on appelle l'Immortelle.
[p {IMM}] Les Blancs ont déjà laissé un fou. Et ce n'est que le début.
[p {IMM} h4 Qg6 h5 Qg5 Qf3 Ng8 Bxf4 Qf6 Nc3 Bc5] Cavalier [m Nd5 bon] d5. La dame noire prend [m Qxb2] b2 et attaque la tour a1.
Anderssen s'en fiche. Fou [m Bd6 meilleur] d6 ! [m Bxg1] Les Noirs prennent la tour g1. Pion [m e5] e5.
[m Qxa1+] Et la dame prend l'autre tour, échec. Deux tours en moins. Roi [m Ke2] e2, [m Na6] cavalier a6.
Cavalier prend [m Nxg7+] g7, échec, [m Kd8] roi d8. Et maintenant, dame [m Qf6+ meilleur] f6, échec ! Il donne aussi sa dame.
[m Nxf6] Le cavalier prend, et fou [m Be7# mat] e7. Échec et mat, avec trois petites pièces.
Tu veux savoir quelles erreurs te coûtent tes parties ? Analyse-les gratuitement sur BlunderCheck."""),

"rafale1": ("blancs", """Cinq positions. À chaque fois, un seul coup fait mat. Tu as trois secondes.
[p fen:6k1/5ppp/8/8/8/8/5PPP/3R2K1_w_-_-_0_1] Un. Les Blancs jouent. Trois… deux… un… Tour [m Rd8# mat] d8 ! Le roi est enfermé par ses propres pions.
[p fen:6rk/6pp/8/6N1/8/8/6PP/6K1_w_-_-_0_1] Deux. Les Blancs jouent. Trois… deux… un… Cavalier [m Nf7# mat] f7 ! Le mat à l'étouffée.
[p e4 e5 Bc4 Nc6 Qh5 Nf6] Trois. Les Blancs jouent. Trois… deux… un… Dame prend [m Qxf7# mat] f7 ! Le coup du berger.
[p fen:7k/8/5K2/8/8/8/8/6Q1_w_-_-_0_1] Quatre. Les Blancs jouent. Trois… deux… un… Dame [m Qg7# mat] g7 ! Protégée par le roi.
[p fen:3r2k1/8/8/8/8/8/5PPP/6K1_b_-_-_0_1] Cinq. Cette fois, ce sont les Noirs. Trois… deux… un… Tour [m Rd1# mat] d1 ! Le mat du couloir.
Alors, combien sur cinq ? Dis-le en commentaire. Et pour t'entraîner sur tes propres erreurs, analyse tes parties gratuitement sur BlunderCheck."""),

"rafale2": ("blancs", """Cinq mats en un, niveau deux. Ils viennent tous de pièges et de parties célèbres. Trois secondes à chaque fois.
[p e4 e5 Nf3 d6 Bc4 Bg4 Nc3 g6 Nxe5 Bxd1 Bxf7+ Ke7] Un. Les Blancs jouent. Trois… deux… un… Cavalier [m Nd5# mat] d5 ! Le mat de Légal.
[p e4 c6 d4 d5 Nc3 dxe4 Nxe4 Nd7 Qe2 Ngf6] Deux. Les Blancs jouent. Trois… deux… un… Cavalier [m Nd6# mat] d6 ! Le pion e7 est cloué.
[p e4 c5 d4 cxd4 c3 dxc3 Nxc3 Nc6 Nf3 e6 Bc4 Qc7 O-O Nf6 Qe2 Ng4 h3 Nd4 Nxd4] Trois. Les Noirs jouent. Trois… deux… un… Dame [m Qh2# mat] h2 ! Le piège sibérien.
[p d4 Nf6 c4 e5 dxe5 Ng4 Bf4 Nc6 Nf3 Bb4+ Nbd2 Qe7 a3 Ngxe5 axb4] Quatre. Les Noirs jouent. Trois… deux… un… Cavalier [m Nd3# mat] d3 ! Le pion e2 ne peut pas prendre : il est cloué par la dame.
[p e4 e5 Nf3 d6 d4 Bg4 dxe5 Bxf3 Qxf3 dxe5 Bc4 Nf6 Qb3 Qe7 Nc3 c6 Bg5 b5 Nxb5 cxb5 Bxb5+ Nbd7 O-O-O Rd8 Rxd7 Rxd7 Rd1 Qe6 Bxd7+ Nxd7 Qb8+ Nxb8] Cinq. Les Blancs jouent. Trois… deux… un… Tour [m Rd8# mat] d8 ! La fin de la partie de l'Opéra.
Combien sur cinq ? Dis-le en commentaire. Et analyse tes propres parties gratuitement sur BlunderCheck."""),

"rafale3": ("blancs", """Quatre mats en un, niveau trois. Trois secondes à chaque fois.
[p d4 e5 dxe5 Nc6 Nf3 Qe7 Bf4 Qb4+ Bd2 Qxb2 Bc3 Bb4 Qd2 Bxc3 Qxc3] Un. Le gambit Englund. Les Noirs jouent. Trois… deux… un… Dame [m Qc1# mat] c1 !
[p e4 e5 Nf3 Nf6 Nxe5 Nc6 Nxc6 dxc6 d3 Bc5 Bg5 Nxe4 Bxd8 Bxf2+ Ke2] Deux. Le gambit Stafford. Les Noirs jouent. Trois… deux… un… Fou [m Bg4# mat] g4 ! Les Blancs ont pris la dame, et ils sont mat.
[p e4 e5 Nf3 Nc6 Bc4 Nd4 Nxe5 Qg5 Nxf7 Qxg2 Rf1 Qxe4+ Be2] Trois. Le piège Blackburne. Les Noirs jouent. Trois… deux… un… Cavalier [m Nf3# mat] f3 !
[p e4 c6 d4 d5 Nc3 dxe4 Nxe4 Nf6 Qd3 e5 dxe5 Qa5+ Bd2 Qxe5 O-O-O Nxe4 Qd8+ Kxd8 Bg5+ Kc7] Quatre. Réti contre Tartakower. Les Blancs jouent. Trois… deux… un… Fou [m Bd8# mat] d8 ! Un grand maître, mat en onze coups.
Tu les as tous trouvés ? Dis-le en commentaire. Et analyse tes propres parties gratuitement sur BlunderCheck."""),
})
