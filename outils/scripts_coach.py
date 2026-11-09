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

# ---------- lot 3 : formats viraux US adaptés (21/10, 17 h 30) ----------
FISCH = "Nf3 Nf6 c4 g6 Nc3 Bg7 d4 O-O Bf4 d5 Qb3 dxc4 Qxc4 c6 e4 Nbd7 Rd1 Nb6 Qc5 Bg4 Bg5 Na4 Qa3 Nxc3 bxc3 Nxe4 Bxe7 Qb6 Bc4 Nxc3 Bc5 Rfe8+ Kf1"
FISCH_FIN = FISCH + " Be6 Bxb6 Bxc4+ Kg1 Ne2+ Kf1 Nxd4+ Kg1 Ne2+ Kf1 Nc3+ Kg1 axb6 Qb4 Ra4 Qxb6 Nxd1 h3 Rxa2 Kh2 Nxf2 Re1 Rxe1 Qd8+ Bf8 Nxe1 Bd5 Nf3 Ne4 Qb8 b5 h4 h5 Ne5 Kg7 Kg1 Bc5+ Kf1 Ng3+ Ke1 Bb4+ Kd1 Bb3+ Kc1 Ne2+ Kb1 Nc3+ Kc1"
KASP = "e4 d6 d4 Nf6 Nc3 g6 Be3 Bg7 Qd2 c6 f3 b5 Nge2 Nbd7 Bh6 Bxh6 Qxh6 Bb7 a3 e5 O-O-O Qe7 Kb1 a6 Nc1 O-O-O Nb3 exd4 Rxd4 c5 Rd1 Nb6 g3 Kb8 Na5 Ba8 Bh3 d5 Qf4+ Ka7 Rhe1 d4 Nd5 Nbxd5 exd5 Qd6"
KASP_FIN = KASP + " Rxd4 cxd4 Re7+ Kb6 Qxd4+ Kxa5 b4+ Ka4 Qc3 Qxd5 Ra7 Bb7 Rxb7 Qc4 Qxf6 Kxa3 Qxa6+ Kxb4 c3+ Kxc3 Qa1+ Kd2 Qb2+ Kd1 Bf1 Rd2 Rd7 Rxd7 Bxc4 bxc4 Qxh8 Rd3 Qa8 c3 Qa4+ Ke1 f4 f5 Kc1 Rd2 Qa7"
BODEN = "e4 e5 Nf3 d6 c3 f5 Bc4 Nf6 d4 fxe4 dxe5 exf3 exf6 Qxf6 gxf3 Nc6 f4 Bd7 Be3 O-O-O Nd2 Re8 Qf3 Bf5"
SCRIPTS.update({
"v_stafford": ("noirs", """Ce piège a rendu Eric Rosen célèbre sur Internet. Son nom : oh no, my queen.
[m e4] e4, [m e5] e5, cavalier [m Nf3] f3, cavalier [m Nf6 livre] f6. Les Blancs prennent [m Nxe5] e5, et toi, cavalier [m Nc6 bizarre] c6 ! C'est le gambit Stafford : tu donnes un pion.
Cavalier prend [m Nxc6] c6, d prend [m dxc6] c6. Tes pièces sortent toutes seules. [m d3] d3, fou [m Bc5] c5.
Et là, les Blancs attaquent ta dame : fou [m Bg5 gaffe] g5. Tout le monde pense que ta dame est perdue.
[q 3 Trouve_le_coup_des_Noirs] Mais tu joues cavalier prend [m Nxe4 meilleur] e4 ! Tu laisses ta dame. Fou prend [m Bxd8] d8 : oh no, my queen.
Fou prend [m Bxf2+] f2, échec. Le roi doit aller [m Ke2] en e2, et fou [m Bg4# mat] g4. Échec et mat.
Le bon coup pour les Blancs, c'était [p e4 e5 Nf3 Nf6 Nxe5 Nc6 Nxc6 dxc6 d3 Bc5] fou [m Be2 meilleur] e2. Le Stafford gagne vite, mais il perd contre la bonne défense.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_englund": ("noirs", """Le gambit Englund. Une ouverture douteuse… qui cache un piège mortel.
[m d4] d4, [m e5 bizarre] e5 ! Tu donnes un pion. d prend [m dxe5] e5, cavalier [m Nc6] c6, cavalier [m Nf3] f3, dame [m Qe7] e7.
Fou [m Bf4] f4 pour défendre le pion. Et là, dame [m Qb4+ bon] b4, échec ! Elle vise aussi b2. Fou [m Bd2] d2, dame prend [m Qxb2] b2.
La tour a1 est attaquée. Le réflexe des Blancs : fou [m Bc3 gaffe] c3, pour chasser ta dame. Erreur fatale.
[q 3 Trouve_le_coup_des_Noirs] Fou [m Bb4 meilleur] b4 ! Tu cloues le fou contre le roi. Dame [m Qd2] d2 pour le protéger, fou prend [m Bxc3] c3, dame prend [m Qxc3] c3.
Et dame [m Qc1# mat] c1. Échec et mat.
Le bon coup, c'était [p d4 e5 dxe5 Nc6 Nf3 Qe7 Bf4 Qb4+ Bd2 Qxb2] cavalier [m Nc3 meilleur] c3.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_lasker": ("noirs", """Le piège de Lasker. Il finit par un coup que tu ne verras presque jamais : une promotion en cavalier.
Contre le gambit dame, [m d4] d4, [m d5] d5, [m c4] c4, tu joues [m e5 bizarre] e5 : le contre-gambit Albin.
d prend [m dxe5] e5, [m d4] d4. Ce pion gêne énormément les Blancs. Ils jouent [m e3 erreur] e3 pour s'en débarrasser.
Fou [m Bb4+] b4, échec, fou [m Bd2] d2, d prend [m dxe3] e3. Et les Blancs prennent ton fou : [m Bxb4 gaffe] fou prend b4. Grave erreur.
e prend [m exf2+ bon] f2, échec. Le roi va [m Ke2] en e2. Et maintenant : f prend [m fxg1=N+ meilleur] g1, et le pion devient… un cavalier ! Échec !
Une dame en g1 ne donnait pas échec. Le cavalier, si. Roi [m Ke1] e1, dame [m Qh4+] h4, échec, et l'attaque noire est gagnante.
Le bon coup, c'était [p d4 d5 c4 e5 dxe5 d4 e3 Bb4+ Bd2 dxe3] f prend [m fxe3 meilleur] e3.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_noe": ("noirs", """Le piège de l'arche de Noé. Il est très ancien, et il attrape encore des joueurs tous les jours.
Partie espagnole : [m e4] e4, [m e5] e5, cavalier [m Nf3] f3, cavalier [m Nc6] c6, fou [m Bb5] b5, [m a6] a6, fou [m Ba4] a4, [m d6] d6.
[m d4] d4, [m b5] b5, fou [m Bb3] b3. Et là, cavalier prend [m Nxd4 bizarre] d4 ! Cavalier [m Nxd4] reprend, e prend [m exd4] d4.
Les Blancs reprennent avec la dame : [m Qxd4 gaffe] dame prend d4. Erreur. [q 3 Trouve_le_coup_des_Noirs] Pion [m c5 bon] c5 ! La dame doit partir, [m Qd5] en d5, pour attaquer la tour a8.
Fou [m Be6] e6, dame [m Qc6+] c6, échec, fou [m Bd7] d7, dame [m Qd5] d5. Et pion [m c4 meilleur] c4.
Le fou b3 est enfermé : tes pions b5 et c4 le bloquent, et ses propres pions a2 et c2 aussi. Il est perdu.
Le bon coup, c'était [p e4 e5 Nf3 Nc6 Bb5 a6 Ba4 d6 d4 b5 Bb3 Nxd4 Nxd4 exd4] [m c3 meilleur] c3 : on donne un pion, pas une pièce.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_mortimer": ("noirs", """Le piège Mortimer. Tu laisses un pion en prise… exprès.
Partie espagnole, défense berlinoise : [m e4] e4, [m e5] e5, cavalier [m Nf3] f3, cavalier [m Nc6] c6, fou [m Bb5] b5, cavalier [m Nf6] f6.
Les Blancs jouent tranquille, [m d3] d3. Et toi, cavalier [m Ne7 bizarre] e7 ! Un coup bizarre. Le pion e5 n'est plus défendu.
Les Blancs le prennent : cavalier prend [m Nxe5 gaffe] e5. Et là, [m c6 meilleur] c6 ! Le fou b5 est attaqué.
Si le fou recule [m Bc4] en c4, dame [m Qa5+ bon] a5, échec, [f a5e5] et ta dame attaque aussi le cavalier e5. Les Blancs perdent une pièce.
Le bon coup, c'était de ne pas toucher au pion : [p e4 e5 Nf3 Nc6 Bb5 Nf6 d3 Ne7] petit roque, [m O-O meilleur] et la partie est égale.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_tarrasch": ("blancs", """Le piège Tarrasch, dans l'espagnole ouverte. Une position très jouée en club.
[p e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Nxe4 d4 b5 Bb3 d5 dxe5 Be6 c3 Be7 Re1 O-O] Les Blancs jouent cavalier [m Nd4 bon] d4. Il attaque le fou e6 et le cavalier c6.
Les Noirs protègent tout avec dame [m Qd7 gaffe] d7. Erreur. Cavalier prend [m Nxe6] e6, f prend [m fxe6] e6.
[q 3 Trouve_le_coup_des_Blancs] Et maintenant : tour prend [m Rxe4 meilleur] e4 ! Le pion d5 est le seul qui bloque la colonne d. [f d1d7]
Si d prend [m dxe4] e4, la colonne s'ouvre, et dame prend [m Qxd7] d7. La dame noire tombe.
Le bon coup pour les Noirs, c'était [p e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Nxe4 d4 b5 Bb3 d5 dxe5 Be6 c3 Be7 Re1 O-O Nd4] cavalier prend [m Nxe5 meilleur] e5.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_siberien": ("noirs", """S'il prend ce cavalier, c'est mat en h2. Voici le piège sibérien, contre le gambit Smith-Morra.
[m e4] e4, [m c5] c5, [m d4] d4, c prend [m cxd4] d4, [m c3] le pion c3 : les Blancs offrent un pion. d prend [m dxc3] c3, cavalier prend [m Nxc3] c3.
[p e4 c5 d4 cxd4 c3 dxc3 Nxc3 Nc6 Nf3 e6 Bc4 Qc7 O-O Nf6 Qe2] Quelques coups plus tard, les Blancs ont roqué, leur dame est en e2.
Tu joues cavalier [m Ng4 bizarre] g4. Il vise h2, [f c7h2] avec ta dame. Les Blancs le chassent : [m h3] h3.
[q 3 Trouve_le_coup_des_Noirs] Et toi, au lieu de reculer : cavalier [m Nd4 bon] d4 ! Tu attaques la dame. Les Blancs prennent : [m Nxd4 gaffe] cavalier prend d4.
Et dame [m Qh2# mat] h2. Échec et mat ! Le cavalier g4 protège ta dame.
Et s'ils avaient pris le cavalier g4, tu prenais leur dame en e2, avec échec.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_kieninger": ("noirs", """Le piège Kieninger, dans le gambit de Budapest.
[m d4] d4, cavalier [m Nf6] f6, [m c4] c4, [m e5 bizarre] e5 ! d prend [m dxe5] e5, cavalier [m Ng4] g4 : tu vas récupérer le pion.
Fou [m Bf4] f4, cavalier [m Nc6] c6, cavalier [m Nf3] f3, fou [m Bb4+] b4, échec, cavalier [m Nbd2] d2, dame [m Qe7] e7.
Les Blancs chassent ton fou : [m a3] a3. [q 3 Trouve_le_coup_des_Noirs] Et tu reprends le pion, cavalier prend [m Ngxe5 bon] e5, en laissant ton fou !
Les Blancs le prennent : [m axb4 gaffe] a prend b4. Et cavalier [m Nd3# mat] d3. Échec et mat !
Le pion e2 pourrait prendre… mais il est cloué par ta dame. [f e7e1]
Le bon coup, c'était [p d4 Nf6 c4 e5 dxe5 Ng4 Bf4 Nc6 Nf3 Bb4+ Nbd2 Qe7 a3 Ngxe5] cavalier prend [m Nxe5 meilleur] e5.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_foiefrit": ("blancs", """L'attaque du foie frit. Une des attaques les plus connues sur Internet.
[m e4] e4, [m e5] e5, cavalier [m Nf3] f3, cavalier [m Nc6] c6, fou [m Bc4] c4, cavalier [m Nf6] f6.
Cavalier [m Ng5 bizarre] g5 ! Tu vises f7 [f g5f7 c4f7] avec deux pièces. Les Noirs bloquent : [m d5] d5, e prend [m exd5] d5.
Et beaucoup reprennent avec le cavalier : [m Nxd5 erreur] cavalier prend d5. [q 3 Trouve_le_coup_des_Blancs] C'est là que tu sacrifies.
Cavalier prend [m Nxf7 bon] f7 ! Le roi [m Kxf7] prend, dame [m Qf3+] f3, échec. Le roi monte [m Ke6] en e6 pour protéger son cavalier.
Cavalier [m Nc3] c3 : tu attaques le cavalier cloué, et le roi noir est au milieu de l'échiquier. Ça, c'est le foie frit.
Pour les Noirs, le bon coup était [p e4 e5 Nf3 Nc6 Bc4 Nf6 Ng5 d5 exd5] cavalier [m Na5 meilleur] a5.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_tennison": ("blancs", """Le gambit Tennison. Peu de gens le connaissent, et c'est pour ça qu'il marche.
Cavalier [m Nf3] f3, [m d5] d5, [m e4 bizarre] e4 ! Tu donnes un pion. d prend [m dxe4] e4, cavalier [m Ng5] g5 : tu vas le récupérer.
Cavalier [m Nf6] f6, [m d3] d3, e prend [m exd3] d3, fou prend [m Bxd3] d3.
Les Noirs veulent chasser ton cavalier : [m h6 gaffe] h6. Erreur. [q 3 Trouve_le_coup_des_Blancs] Cavalier prend [m Nxf7 bon] f7 ! Le roi [m Kxf7] prend… et fou [m Bg6+ meilleur] g6, échec !
Si le roi prend [m Kxg6] le fou, dame prend [m Qxd8] d8. La colonne d s'est ouverte, et la dame noire tombe.
Le bon coup pour les Noirs, c'était [p Nf3 d5 e4 dxe4 Ng5 Nf6 d3 exd3 Bxd3] cavalier [m Nc6 meilleur] c6.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_halosar": ("blancs", """Le piège Halosar, dans le gambit Blackmar-Diemer.
[m d4] d4, [m d5] d5, [m e4 bizarre] e4 ! d prend [m dxe4] e4, cavalier [m Nc3] c3, cavalier [m Nf6] f6, [m f3] f3, e prend [m exf3] f3, dame prend [m Qxf3] f3.
Les Noirs prennent un deuxième pion : dame prend [m Qxd4] d4. Fou [m Be3] e3, dame [m Qb4] b4, et grand roque [m O-O-O] : ta tour arrive sur la colonne d.
Les Noirs attaquent ta dame : fou [m Bg4 gaffe] g4. [q 3 Trouve_le_coup_des_Blancs] Et toi, tu la laisses ! Cavalier [m Nb5 meilleur] b5 ! [f b5c7]
Si le fou prend [m Bxf3] ta dame, cavalier prend [m Nxc7# mat] c7. Échec et mat ! La tour d1 tient la case d8.
Le bon coup pour les Noirs, c'était [p d4 d5 e4 dxe4 Nc3 Nf6 f3 exf3 Qxf3 Qxd4 Be3 Qb4 O-O-O] [m c6 meilleur] c6, qui contrôle b5.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_philidor": ("blancs", """Un piège de la défense Philidor. Philidor, c'était un Français, le meilleur joueur du dix-huitième siècle.
[m e4] e4, [m e5] e5, cavalier [m Nf3] f3, [m d6] d6, [m d4] d4, cavalier [m Nd7] d7, fou [m Bc4] c4.
Les Noirs sortent leur fou : [m Be7 gaffe] e7. Erreur ! d prend [m dxe5] e5, d prend [m dxe5] e5. Dame [m Qd5 meilleur] d5 !
[f d5f7 c4f7] Elle menace dame prend f7, échec et mat. Les Noirs défendent avec cavalier [m Nh6] h6.
Et fou prend [m Bxh6 bon] h6 ! Si g prend h6, dame prend f7, et c'est mat. Les Noirs perdent une pièce.
Le bon coup, c'était [p e4 e5 Nf3 d6 d4 Nd7 Bc4] [m c6 meilleur] c6.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_francaise": ("noirs", """Tu joues la défense française ? Alors ce piège est pour toi.
[m e4] e4, [m e6 livre] e6, [m d4] d4, [m d5] d5, [m e5] e5 : la variante d'avance. [m c5] c5, [m c3] c3, cavalier [m Nc6] c6, cavalier [m Nf3] f3, dame [m Qb6] b6.
Tout le monde attaque d4. Fou [m Bd3] d3, c prend [m cxd4] d4, c prend [m cxd4] d4. Le pion d4 a l'air faible.
Cavalier prend [m Nxd4 gaffe] d4 ? Cavalier [m Nxd4] reprend, dame prend [m Qxd4] d4… et fou [m Bb5+ meilleur] b5, échec !
[f d1d4] La dame d1 voit ta dame. Quoi que tu joues, elle la prend.
Le bon coup, c'était [p e4 e6 d4 d5 e5 c5 c3 Nc6 Nf3 Qb6 Bd3 cxd4 cxd4] fou [m Bd7 meilleur] d7.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_legal": ("blancs", """Le mat de Légal. Légal, c'était un joueur français du dix-huitième siècle, au café de la Régence, à Paris.
[m e4] e4, [m e5] e5, cavalier [m Nf3] f3, [m d6] d6, fou [m Bc4] c4, fou [m Bg4] g4 : il cloue ton cavalier sur ta dame.
Cavalier [m Nc3] c3, [m g6 erreur] g6. Et là, tu fais l'impensable : cavalier prend [m Nxe5 meilleur] e5 ! Tu laisses ta dame.
Les Noirs la prennent : fou prend [m Bxd1 gaffe] d1. Fou prend [m Bxf7+] f7, échec, le roi doit aller [m Ke7] en e7,
et cavalier [m Nd5# mat] d5. Échec et mat avec trois petites pièces.
Pour les Noirs, il fallait reprendre le cavalier, d prend e5 : ils perdaient un pion, pas la partie.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_qga": ("blancs", """Gambit dame accepté. Les Noirs prennent le pion c4… et veulent le garder. Grosse erreur.
[m d4] d4, [m d5] d5, [m c4] c4, d prend [m dxc4] c4, [m e3] e3. Les Noirs défendent leur pion avec [m b5 gaffe] b5.
[m a4] a4 ! Tu attaques la chaîne. [m c6] c6 pour tenir, a prend [m axb5] b5, c prend [m cxb5] b5.
Et maintenant : dame [m Qf3 meilleur] f3 ! [f f3a8] La grande diagonale est ouverte, la dame attaque la tour a8.
Les Noirs ne peuvent pas tout sauver : ils perdent du matériel.
Le bon coup, c'était [p d4 d5 c4 dxc4 e3] cavalier [m Nf6 meilleur] f6, sans s'accrocher au pion.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_bongcloud": ("blancs", """Le champion du monde a ouvert une partie avec le pire coup possible.
Magnus Carlsen contre Hikaru Nakamura, mars 2021, en ligne. [m e4] e4, [m e5] e5. Et Magnus joue… roi [m Ke2 bizarre] e2.
C'est le Bongcloud, une ouverture-blague. Et Nakamura répond pareil : roi [m Ke7 bizarre] e7 !
Roi [m Ke1] e1, roi [m Ke8] e8. Roi [m Ke2] e2, roi [m Ke7] e7. Et ils répètent les coups : nulle.
Pourquoi ? Les deux étaient déjà qualifiés, la partie ne comptait plus. Alors ils se sont amusés.
En vrai, ce roi en e2 bloque ton fou et ta dame, et il perd le droit de roquer. C'est juste mauvais.
Mais quand tu es champion du monde, tu as le droit. Toi, tu joues quoi au premier coup ? Dis-le en commentaire.
Et analyse tes parties gratuitement sur BlunderCheck."""),

"v_fischer": ("noirs", f"""New York, 1956. Bobby Fischer a treize ans. En face, Donald Byrne, un des meilleurs joueurs américains. On l'appelle la partie du siècle.
[p {FISCH}] Au dix-septième coup, la dame noire est attaquée [f c5b6] par le fou c5. Tout le monde attend que Fischer la sauve.
Et il joue fou [m Be6 meilleur] e6 ! Il laisse sa dame. Byrne la prend : fou prend [m Bxb6] b6.
Et Fischer lance un moulin : fou prend [m Bxc4+ bon] c4, échec. Roi [m Kg1] g1, cavalier [m Ne2+] e2, échec, roi [m Kf1] f1,
cavalier prend [m Nxd4+] d4, échec, roi [m Kg1] g1, cavalier [m Ne2+] e2, roi [m Kf1] f1, cavalier [m Nc3+] c3, roi [m Kg1] g1, et a prend [m axb6] b6.
Pour sa dame, Fischer récupère deux fous, un pion, et bientôt une tour.
[p {FISCH_FIN}] Vingt coups plus tard, tour [m Rc2# mat] c2. Échec et mat, par un gamin de treize ans.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_kasparov": ("blancs", f"""Wijk aan Zee, 1999. Kasparov contre Topalov. Pour beaucoup, c'est la plus belle partie de Kasparov.
[p {KASP}] Position tendue. Et Kasparov joue tour prend [m Rxd4 meilleur] d4 ! Il donne une tour.
Topalov [m cxd4] prend. Tour [m Re7+ bon] e7, échec ! Roi [m Kb6] b6, dame prend [m Qxd4+] d4, échec, le roi prend [m Kxa5] le cavalier,
[m b4+] b4, échec, roi [m Ka4] a4. Le roi noir part en promenade… dans le camp blanc. Dame [m Qc3] c3, et la chasse continue.
[p {KASP_FIN}] Le roi noir finit par descendre jusqu'en d1, et Topalov abandonne au quarante-quatrième coup.
Une tour donnée au vingt-quatrième coup, et vingt coups de chasse au roi. Toi, tu aurais osé ?
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_boden": ("noirs", f"""Le mat de Boden. Deux fous qui se croisent, et le roi est mort.
Londres, 1853, Schulder contre Boden. [p {BODEN}] Les Blancs font le grand roque : [m O-O-O erreur] grand roque.
Boden joue [m d5 bon] d5 ! Il ouvre la diagonale de son fou. Si fou prend [m Bxd5] d5 :
dame prend [m Qxc3+ meilleur] c3, échec ! Sacrifice de dame. b prend [m bxc3] c3, et fou [m Ba3# mat] a3. Échec et mat !
Les deux fous, [f f5b1 a3c1] en croix, ferment toutes les cases du roi. C'est le mat de Boden.
Retiens ce dessin : il peut tomber dès que tu fais le grand roque.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_etouffee": ("blancs", """Le mat à l'étouffée. Le plus beau mat des échecs, et il se joue avec un cavalier.
[p fen:r3r2k/pp4pp/8/6N1/2Q5/q7/P4PPP/6K1_w_-_-_0_1] Les Blancs jouent. Cavalier [m Nf7+ bon] f7, échec. Le roi doit aller [m Kg8] en g8.
Cavalier [m Nh6+] h6 : échec double, de la dame et du cavalier ! Le roi retourne [m Kh8] en h8. S'il va en f8, dame f7, c'est mat.
Et maintenant, le coup de génie : dame [m Qg8+ meilleur] g8, échec ! Tu sacrifies ta dame.
Le roi ne peut pas la prendre, le cavalier la protège. Alors la tour [m Rxg8] prend. Et cavalier [m Nf7# mat] f7. Échec et mat !
Le roi est enfermé par ses propres pièces. On l'appelle aussi le legs de Philidor, du nom d'un joueur français.
Analyse tes parties gratuitement sur BlunderCheck."""),
})

# ---------- format PERSO (21/10, 21 h 45) : personnages BlunderCheck, voix expressive, pas de musique ----------
# Repères en plus : [s genre case durée texte?] autocollant (bonbon, couronne, tag), [z case(s) facteur durée] zoom,
# [x son] bruitage, [h] fin du hook (le bandeau fixe s'arrête là). Personnages : la Gourmande (dame adverse),
# les bonbons (pions ou pièces offerts), le poney (cavalier), le pigeon (l'adversaire), toi.
LASKER_PONEY = "d4 d5 c4 e5 dxe5 d4 e3 Bb4+ Bd2 dxe3 Bxb4 exf2+ Ke2 fxg1=N+"
PERSO = {
"perso_lasker": {
    "cote": "noirs",
    "hook": "Arrête de faire une dame.|Ici, fais un poney.",
    # texte lu par ElevenLabs v3 (indications de jeu entre crochets, non prononcées ; cases en toutes lettres)
    "voix": """[mischievously] Arrête de faire une dame à chaque promotion. Ici, tu fais un poney.
[fast] On rembobine. Il joue dé quatre, dé cinq, cé quatre.
Toi, tu lui poses un bonbon : e cinq. Le pigeon le mange. [amused] Miam.
Tu avances dé quatre. Ça le gêne. Il joue e trois.
Fou bé quatre, échec. Fou dé deux. Tu prends e trois.
[whispers] Et là, il voit un gros bonbon : ton fou. [mocking] Il le mange. Erreur !
Tu prends effe deux, échec. Son roi monte en e deux.
Ton pion arrive au bout. Tout le monde fait une dame. Pas toi.
[excited] Tu fais un poney. Échec ! Une dame ? La Gourmande prenait la tienne, avec échec. Fini.
Le poney, lui, donne échec. Pas le temps.
Il prend le poney ? Fou gé quatre, échec. Son roi bouge… [laughs] et la Gourmande tombe.
Il ne le prend pas ? Roi e un, dame hache quatre, échec. Son roi se promène.
[smug] Le pigeon, c'était lui. Analyse tes parties sur BlunderCheck.""",
    "script": """[p d4 d5 c4 e5 dxe5 d4 e3 Bb4+ Bd2 dxe3 Bxb4 exf2+ Ke2] [f f2g1] Arrête de faire une dame à chaque promotion. [s tag e2 3.5 LE_PIGEON] Ici, tu fais un poney.
[h] [p] On rembobine. Il joue [m d4] d4, [m d5] d5, [m c4] c4.
Toi, tu lui poses un bonbon : [m e5 bizarre] e5. [s bonbon e5 2.5] Le pigeon le mange. [m dxe5] Miam.
Tu avances [m d4] d4. Ça le gêne. Il joue [m e3 erreur] e3.
Fou [m Bb4+] b4, échec. Fou [m Bd2] d2. Tu prends [m dxe3] e3.
Et là, il voit un gros bonbon : [s bonbon b4 2.5] ton fou. Il le mange. [m Bxb4 gaffe] Erreur !
Tu prends [m exf2+] f2, échec. Son roi monte [m Ke2] en e2.
Ton pion arrive au bout. [f f2g1] Tout le monde fait une dame. Pas toi.
Tu fais un poney. [m fxg1=N+ brillant] [z e2g1 1.45 2.6] Échec ! [s tag g1 2.5 LE_PONEY]
Une dame ? [s couronne d1 3.5] La Gourmande prenait la tienne, [f d1d8] avec échec. Fini.
Le poney, lui, donne échec. Pas le temps.
Il prend le poney ? [m Rxg1] Fou [m Bg4+ bon] g4, échec. [f g4d1] [s couronne d1 2.6] Son roi bouge, [m Kf2] et la Gourmande [m Bxd1] [z d1 1.6 2.0] [x impact] tombe.
Il ne le prend pas ? [p """ + LASKER_PONEY.replace(" ", " ") + """] Roi [m Ke1] e1, dame [m Qh4+ bon] h4, échec. [z e1 1.4 1.8] Son roi se promène.
Le pigeon, c'était lui. Analyse tes parties sur BlunderCheck.""",
},
"perso_legal": {
    # 22/10 (Simon) : style « bonbon / pigeon » enfantin mais percutant ; la voix ne dit aucune case (pas de souci de prononciation)
    "cote": "blancs",
    "hook": "Donne ta dame au pigeon.|Oui, ta dame.",
    "voix": """[mischievously] Donne ta dame au pigeon. Oui, ta dame entière.
[fast] On rembobine. Ton pion avance de deux cases. Il fait pareil. Ton poney sort. Lui avance un petit pion. Ton fou sort et vise son roi.
Son fou sort aussi, et il cloue ton poney sur ta dame. [mocking] Il est fier.
Ton deuxième poney sort. Lui joue un petit pion, sans réfléchir.
[whispers] Et là, tu lui tends le plus gros bonbon du monde. Ton poney mange son pion, et tu laisses ta dame.
[amused] Le pigeon la voit toute seule. Il la mange. Miam.
[excited] Ton fou fonce : échec ! Son roi n'a qu'une case.
Ton deuxième poney saute. [laughs] Échec et mat. Avec trois petites pièces.
[smug] Il a mangé ta dame. Toi, tu as mangé la partie. Analyse tes parties sur BlunderCheck.""",
    "script": """[p e4 e5 Nf3 d6 Bc4 Bg4 Nc3 g6 Nxe5] [f g4d1] Donne ta dame au pigeon. [s tag d1 3.0 CADEAU] Oui, ta dame entière.
[h] [p] On rembobine. Ton pion [m e4] avance de deux cases. Il fait [m e5] pareil. Ton poney [m Nf3] sort. Lui avance un [m d6] petit pion. Ton fou [m Bc4] sort [f c4f7] et vise son roi.
Son fou sort aussi, [m Bg4] et il cloue ton poney [f g4d1] sur ta dame. Il est fier.
Ton deuxième poney [m Nc3] sort. Lui joue un petit pion, [m g6 erreur] sans réfléchir.
Et là, tu lui tends le plus gros bonbon du monde. [s bonbon d1 3.0] Ton poney mange son pion, [m Nxe5 brillant] et tu laisses ta dame.
Le pigeon la voit toute seule. Il la mange. [m Bxd1 gaffe] Miam. [s tag d1 2.5 LE_PIGEON]
Ton fou fonce : [m Bxf7+] échec ! Son roi n'a qu'une case. [m Ke7]
Ton deuxième poney saute. [m Nd5# mat] [z e7d5 1.45 2.6] [x impact] Échec et mat. Avec trois petites pièces.
Il a mangé ta dame. Toi, tu as mangé la partie. Analyse tes parties sur BlunderCheck.""",
},
}

# ---------- hooks affichés dès l'image 1 (règle 2) pour les scripts coach ; le bandeau tient jusqu'à la fin de la 1re phrase ----------
HOOKS = {
    "v_stafford": "Il prend ta dame…|et il se fait mater.",
    "v_englund": "Ce gambit douteux|fait mat en 8 coups.",
    "v_noe": "Ton fou peut être|enfermé vivant.",
    "v_halosar": "Il laisse sa dame…|et fait mat.",
    "v_foiefrit": "Tu connais|l'attaque du foie frit ?",
    "v_kieninger": "Prends ce fou|et c'est mat en d3.",
    "v_tennison": "Sa dame tombe|en 8 coups.",
    "v_tarrasch": "Le piège qui gagne la dame|dans l'espagnole.",
    "v_siberien": "Il prend ce cavalier ?|Mat en h2.",
    "v_mortimer": "Laisse ce pion en prise.|Exprès.",
}

# ---------- image 1 = la position finale (règle 3), montrée sous le hook avant de rembobiner ----------
TEASERS = {
    "v_siberien": "e4 c5 d4 cxd4 c3 dxc3 Nxc3 Nc6 Nf3 e6 Bc4 Qc7 O-O Nf6 Qe2 Ng4 h3 Nd4 Nxd4 Qh2#",
    "v_stafford": "e4 e5 Nf3 Nf6 Nxe5 Nc6 Nxc6 dxc6 d3 Bc5 Bg5 Nxe4 Bxd8 Bxf2+ Ke2 Bg4#",
    "v_englund": "d4 e5 dxe5 Nc6 Nf3 Qe7 Bf4 Qb4+ Bd2 Qxb2 Bc3 Bb4 Qd2 Bxc3 Qxc3 Qc1#",
    "v_noe": "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 d6 d4 b5 Bb3 Nxd4 Nxd4 exd4 Qxd4 c5 Qd5 Be6 Qc6+ Bd7 Qd5 c4",
    "v_halosar": "d4 d5 e4 dxe4 Nc3 Nf6 f3 exf3 Qxf3 Qxd4 Be3 Qb4 O-O-O Bg4 Nb5 Bxf3 Nxc7#",
    "v_foiefrit": "e4 e5 Nf3 Nc6 Bc4 Nf6 Ng5 d5 exd5 Nxd5 Nxf7 Kxf7 Qf3+ Ke6 Nc3",
    "v_kieninger": "d4 Nf6 c4 e5 dxe5 Ng4 Bf4 Nc6 Nf3 Bb4+ Nbd2 Qe7 a3 Ngxe5 axb4 Nd3#",
    "v_tennison": "Nf3 d5 e4 dxe4 Ng5 Nf6 d3 exd3 Bxd3 h6 Nxf7 Kxf7 Bg6+ Kxg6 Qxd8",
    "v_tarrasch": "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Nxe4 d4 b5 Bb3 d5 dxe5 Be6 c3 Be7 Re1 O-O Nd4 Qd7 Nxe6 fxe6 Rxe4 dxe4 Qxd7",
}
# ---------- question affichée sur les dernières secondes (pousse aux commentaires) ----------
QUESTIONS = {}
QUESTION_DEFAUT = "Tu l'aurais vu ?|Réponds en commentaire."

# ---------- file du 22-23/10 (scénariste) : test FIN (pigeon_jour #1 A, #2 B), quiz_legal #2, ANALYSE n° 1 ----------
# Coups vérifiés python-chess + Stockfish 19 par le producteur (23/10, 1 h). Aucune case dite.
PIGEON1 = "e4 e5 Nf3 Nc6 Bb5 Nf6 O-O Ng4 h3 h5 hxg4 hxg4 Ne1 Qh4 f3 g3 d4 Qh2#"
PIGEON2 = "e4 e5 Nf3 Nc6 Bc4 Nd4 Nxe5 Qg5 Nxf7 Qxg2 Rf1 Qxe4+ Be2 Nf3#"
KRAMNIK_34 = "d4 d5 c4 dxc4 e4 b5 a4 c6 Nc3 b4 Na2 Nf6 e5 Nd5 Bxc4 e6 Nf3 a5 Bg5 Qb6 Nc1 Ba6 Qe2 h6 Be3 Bxc4 Qxc4 Nd7 Nb3 Be7 Rc1 O-O O-O Rfc8 Qe2 c5 Nfd2 Qc6 Qh5 Qxa4 Nxc5 Nxc5 dxc5 Nxe3 fxe3 Bxc5 Qxf7+ Kh8 Qf3 Rf8 Qe4 Qd7 Nb3 Bb6 Rfd1 Qf7 Rf1 Qa7 Rxf8+ Rxf8 Nd4 a4 Nxe6 Bxe3+ Kh1 Bxc1 Nxf8"
PERSO.update({
"pigeon_jour_1": {
    "cote": "noirs",
    "hook": "S'il mange ton poney,|il est mat.",
    "voix": """[mischievously] S'il mange ton poney, il est mat.
[fast] Tu as les Noirs. Ton poney saute tout près de son roi. Le pigeon le chasse avec un pion.
Toi, tu ne bouges pas. [whispers] Tu avances un pion juste à côté.
[amused] Il mange ton poney. Le plus gros bonbon du monde. Tu reprends.
[excited] Et là, une autoroute s'ouvre vers son roi. Ta dame fonce. Ton pion pousse encore.
Ta dame plonge à côté de son roi. [laughs] Mat.
[smug] Il a mangé ton poney. Toi, tu as mangé la partie.
Tu serais tombé dedans ? Commente A : oui, ou B : jamais.""",
    "script": """[p e4 e5 Nf3 Nc6 Bb5 Nf6 O-O Ng4 h3 h5 hxg4 hxg4 Ne1 Qh4 f3 g3 d4 Qh2#] [s tag h2 3.0 MAT] S'il mange ton poney, il est mat.
[h] [p e4 e5 Nf3 Nc6 Bb5 Nf6 O-O] Tu as les Noirs. Ton poney saute [m Ng4 bizarre] tout près de son roi. Le pigeon le chasse [m h3] avec un pion.
Toi, tu ne bouges pas. [s bonbon g4 3.0] Tu avances [m h5 brillant] un pion juste à côté.
Il mange [m hxg4 gaffe] ton poney. [s tag g4 2.5 LE_PIGEON] Le plus gros bonbon du monde. Tu [m hxg4] reprends.
Et là, [m Ne1] une autoroute s'ouvre [f h8h2] vers son roi. Ta dame [m Qh4] fonce. Ton pion [m f3] pousse [m g3] encore.
Ta dame [m d4] plonge [m Qh2# mat] [z h2 1.45 2.6] [x impact] à côté de son roi. Mat.
Il a mangé ton poney. Toi, tu as mangé la partie.
Tu serais tombé dedans ? Commente A : oui, ou B : jamais.""",
},
"pigeon_jour_2": {
    "cote": "noirs",
    "hook": "S'il mange ce bonbon,|il est mat.",
    "voix": """[mischievously] S'il mange ce bonbon, il est mat.
[fast] Tu as les Noirs. Tu laisses un pion tout seul au milieu. Un bonbon.
[amused] Le poney du pigeon le mange. Puis il en mange un deuxième et attaque ta dame et ta tour.
[mocking] Il se croit malin. Ta dame s'en fiche. Elle mange un pion. Elle en mange un deuxième. Échec.
Il cache son roi derrière son fou. [excited] Et là, ton poney saute. [laughs] Mat.
[smug] Il a mangé tes bonbons. Toi, tu as mangé la partie.
Tes pièges à toi, le prof les trouve. Analyse ta partie : lien en bio.""",
    "script": """[p e4 e5 Nf3 Nc6 Bc4 Nd4 Nxe5 Qg5 Nxf7 Qxg2 Rf1 Qxe4+ Be2 Nf3#] [s tag f3 3.0 MAT] S'il mange ce bonbon, il est mat.
[h] [p e4 e5 Nf3 Nc6 Bc4] Tu as les Noirs. Tu laisses [m Nd4 bizarre] un pion tout seul au milieu. [s bonbon e5 2.5] Un bonbon.
Le poney du pigeon [m Nxe5 gaffe] le mange. [s tag e5 2.0 LE_PIGEON] [m Qg5] Puis il en mange [m Nxf7] un deuxième et attaque [f f7g5 f7h8] ta dame et ta tour.
Il se croit malin. Ta dame s'en fiche. Elle mange [m Qxg2] un pion. [m Rf1] Elle en mange [m Qxe4+] un deuxième. Échec.
Il cache son roi [m Be2] derrière son fou. Et là, ton poney [m Nf3# mat] [z f3e1 1.45 2.6] [x impact] saute. Mat.
Il a mangé tes bonbons. Toi, tu as mangé la partie.
Tes pièges à toi, le prof les trouve. Analyse ta partie : lien en bio.""",
},
"quiz_legal_2": {
    "cote": "blancs",
    "hook": "Ton pion devient poney|et fait mat : légal ?",
    "voix": """[mischievously] Ton pion devient poney et fait mat. Légal ou pas ?
Regarde. Son roi s'est caché dans un coin, entouré de ses bonbons, de son fou et de la Gourmande.
Ton pion arrive au bout. Tout le monde prend une dame. Pas toi. [whispers] Tu choisis… un poney.
[excited] Le poney saute : échec. Le roi ne peut aller nulle part, ses propres pièces le bloquent. [laughs] Mat.
Légal ou pas ? Réponds en un mot. … [excited] Légal ! Tu peux changer ton pion en n'importe quelle pièce, même en poney.
Et avec une dame, ici, ce n'était même pas échec. [smug] Tu aurais pris la dame ? Oui ou non ?""",
    "script": """[p fen:6bq/5Ppk/6pp/8/8/8/8/2K5_w_-_-_0_1] [s tag f7 3.0 TON_PION] Ton pion devient poney et fait mat. Légal ou pas ?
[h] Regarde. Son roi s'est caché [z h7 1.4 2.2] dans un coin, entouré de ses bonbons, [s bonbon g6 2.5] de son fou et de la Gourmande. [s couronne h8 2.5]
Ton pion arrive [f f7f8] au bout. Tout le monde prend une dame. Pas toi. Tu choisis… un poney.
[m f8=N# mat] [z h7f8 1.45 2.6] [x impact] Le poney saute : échec. Le roi ne peut aller nulle part, ses propres pièces le bloquent. Mat.
Légal ou pas ? Réponds en un mot. … [q 2 Légal_ou_pas_?] Légal ! Tu peux changer ton pion en n'importe quelle pièce, même en poney.
Et avec une dame, ici, ce n'était même pas échec. Tu aurais pris la dame ? Oui ou non ?""",
},
"analyse_celebre_1": {
    # Deep Fritz – Kramnik, Bonn, 27/11/2006, partie 2 : 34…Qe3?? 35.Qh7# (PGN : chessprogramming.org ; Stockfish : 0.00 avant, mat en 1 après)
    "cote": "blancs",
    "hook": "Tu vois le mat en un|qu'il n'a pas vu ?",
    "voix": """[curious] Tu vois le mat en un qu'il n'a pas vu ?
2006. Un champion du monde contre un ordinateur.
Sa dame part à l'attaque, loin de son roi.
[whispers] Et derrière son dos, la dame de l'ordinateur se glisse à côté de son roi. [excited] Mat. En un coup.
Passe la partie dans BlunderCheck : la gaffe sort en rouge, double point d'interrogation.
[amused] Même les champions font le pigeon. Tu l'avais vu ? Oui ou non ?""",
    "script": """[p d4 d5 c4 dxc4 e4 b5 a4 c6 Nc3 b4 Na2 Nf6 e5 Nd5 Bxc4 e6 Nf3 a5 Bg5 Qb6 Nc1 Ba6 Qe2 h6 Be3 Bxc4 Qxc4 Nd7 Nb3 Be7 Rc1 O-O O-O Rfc8 Qe2 c5 Nfd2 Qc6 Qh5 Qxa4 Nxc5 Nxc5 dxc5 Nxe3 fxe3 Bxc5 Qxf7+ Kh8 Qf3 Rf8 Qe4 Qd7 Nb3 Bb6 Rfd1 Qf7 Rf1 Qa7 Rxf8+ Rxf8 Nd4 a4 Nxe6 Bxe3+ Kh1 Bxc1 Nxf8] [s tag h8 3.0 ROI_NOIR] Tu vois le mat en un qu'il n'a pas vu ?
[h] 2006. Un champion du monde contre un ordinateur.
Sa dame [m Qe3 gaffe] part à l'attaque, loin de son roi.
Et derrière son dos, [f e4h7] la dame de l'ordinateur se glisse [m Qh7# mat] [z h7 1.5 2.6] [x impact] à côté de son roi. Mat. En un coup.
Passe la partie dans BlunderCheck : la gaffe sort en rouge, double point d'interrogation.
Même les champions font le pigeon. Tu l'avais vu ? Oui ou non ?""",
    "musique": 0.0,
},
})
QUESTIONS.update({
    "pigeon_jour_1": "A = oui · B = jamais.|Commente !",
    "pigeon_jour_2": "Analyse ta partie :|lien en bio",
    "quiz_legal_2": "Tu aurais pris la dame ?|Oui ou non ?",
    "analyse_celebre_1": "Analyse ta partie :|lien dans la bio",
})

# ---------- file du 23-24/10 (scénariste) : T1-fin (pigeon_jour #3 A, #4 B), T6-durée (quiz_legal #3 long/court, sans voix), pigeon_en #1-#2 ----------
# Coups vérifiés python-chess 1.11.2 + Stockfish 19 (WASM) par le producteur (24/10, 1 h) : 5 mats confirmés. Aucune case dite.
LEGAL_PIEGE = "e4 e5 Nf3 d6 Bc4 Bg4 Nc3 g6 Nxe5 Bxd1"          # + Bxf7+ Ke7 Nd5#
KIENINGER = "d4 Nf6 c4 e5 dxe5 Ng4 Bf4 Nc6 Nf3 Bb4+ Nbd2 Qe7 a3 Ngxe5 axb4"   # + Nd3#
EP_AVANT = "fen:1Q6/1N1pk3/8/4PQ2/8/8/8/K7_b_-_-_0_1"           # les Noirs jouent d5, puis exd6# (en passant)
EP_APRES = "fen:1Q6/1N2k3/8/3pPQ2/8/8/8/K7_w_-_d6_0_2"
PERSO.update({
"pigeon_jour_3": {
    "cote": "blancs",
    "hook": "S'il mange ta dame,|il est mat.",
    "voix": """[mischievously] S'il mange ta dame, il est mat.
Tu as les Blancs. Ton poney avale un pion. Le pigeon voit ta dame sans défense. Le plus gros bonbon du monde. Il la mange.
Ton fou croque un pion, échec. Son roi avance. Ton poney saute. Mat.
Tu serais tombé dedans ? Commente A : oui, ou B : jamais.""",
    "script": """[p e4 e5 Nf3 d6 Bc4 Bg4 Nc3 g6 Nxe5 Bxd1] [s tag d1 3.0 LE_PIGEON] S'il mange ta dame, il est mat.
[h] [p e4 e5 Nf3 d6 Bc4 Bg4 Nc3 g6] Tu as les Blancs. Ton poney [m Nxe5 brillant] avale un pion. Le pigeon voit [f g4d1] ta dame sans défense. [s bonbon d1 2.5] Le plus gros bonbon du monde. Il la [m Bxd1 gaffe] mange.
Ton fou [m Bxf7+] croque un pion, échec. Son roi [m Ke7] avance. Ton poney [m Nd5# mat] [z d5e7 1.45 2.6] [x impact] saute. Mat.
Tu serais tombé dedans ? Commente A : oui, ou B : jamais.""",
},
"pigeon_jour_4": {
    "cote": "noirs",
    "hook": "S'il mange ton fou,|il est mat.",
    "voix": """[mischievously] S'il mange ton fou, il est mat.
Tu as les Noirs. Tu offres un pion. Il le mange. Ton poney vise ce pion. Ton fou donne échec.
Son pion attaque ton fou. Laisse-le faire. Ton poney reprend. Il mange ton fou. Mat du poney.
Tu serais tombé dedans ? Suis le compte pour la suite.""",
    "script": """[p d4 Nf6 c4 e5 dxe5 Ng4 Bf4 Nc6 Nf3 Bb4+ Nbd2 Qe7 a3 Ngxe5 axb4] [s tag b4 3.0 LE_PIGEON] S'il mange ton fou, il est mat.
[h] [p d4 Nf6 c4] Tu as les Noirs. Tu offres [m e5 bizarre] un pion. Il le [m dxe5] mange. Ton poney [m Ng4] vise [m Bf4] ce [m Nc6] pion. [m Nf3] Ton fou donne [m Bb4+] échec.
[m Nbd2] Son [m Qe7] pion [m a3] attaque ton fou. Laisse-le faire. [s bonbon b4 2.5] Ton poney [m Ngxe5 brillant] reprend. Il [m axb4 gaffe] mange ton fou. [s tag b4 2.0 LE_PIGEON] Mat [m Nd3# mat] [z d3e1 1.45 2.6] [x impact] du poney.
Tu serais tombé dedans ? Suis le compte pour la suite.""",
},
"quiz_legal_3_long": {   # SANS VOIX (commande "muet") : sous-titres en phrases + musique
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Ton pion mange le vide|et fait mat. Légal ?",
    "voix": """Ton pion mange le vide et fait mat. Légal ?
Le pigeon pousse son pion de deux cases. Tes deux dames et ton poney attendent.
Ton pion mange… un pion qui n'est plus là. Légal ou pas ?
Une dame peut mater ? Oui. Mais ce n'est pas la question. Ton poney ? Il ne fait rien. La question, c'est ton pion.
Mat. LÉGAL ! Juste après un saut de deux cases, ton pion peut le manger au passage. Son nom : la prise en passant.
Et si tu joues autre chose d'abord ? Ton roi bouge. Le pion est toujours là. Trop tard. Une seule chance.
Tu le savais ? Oui ou non ?""",
    "script": """[p """ + EP_APRES.replace(" ", "_") + """] [f e5d6] [s tag d5 3.0 LE_PIGEON] Ton pion mange le vide et fait mat. Légal ?
[h] [p """ + EP_AVANT + """] Le pigeon pousse [m d5 bizarre] son pion de deux cases. [s tag d5 2.5 LE_PIGEON] Tes deux dames et ton poney attendent. [z e5 1.3 2.5]
Ton pion mange… un pion qui n'est plus là. Légal ou pas ? [q 3 Légal_ou_pas_?]
Une dame peut [f b8d8] mater ? Oui. Mais ce n'est pas la question. Ton poney ? [f b7d8] Il ne fait rien. La question, c'est [f e5d6] ton pion.
[m exd6# mat] [z d6e7 1.45 2.6] [x impact] Mat. LÉGAL ! Juste après un saut de deux cases, ton pion peut le manger au passage. Son nom : la prise en passant.
[p """ + EP_APRES + """] Et si tu joues autre chose d'abord ? Ton roi [m Ka2] bouge. Le pion est toujours là. [s tag d5 2.5 TROP_TARD] Trop tard. Une seule chance.
Tu le savais ? Oui ou non ?""",
},
"quiz_legal_3_court": {  # SANS VOIX : même position, sans rembobinage, sans fausses pistes, sans rebondissement final
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Ton pion mange le vide|et fait mat. Légal ?",
    "voix": """Ton pion mange le vide et fait mat. Légal ?
Le pigeon vient de pousser son pion de deux cases.
Ton pion mange au passage. Légal ou pas ?
Mat. Légal !
Tu le savais ? Oui ou non ?""",
    "script": """[p """ + EP_APRES + """] [f e5d6] [s tag d5 3.0 LE_PIGEON] Ton pion mange le vide et fait mat. Légal ?
[h] Le pigeon vient de pousser son pion de deux cases. [z d5 1.3 2.0]
Ton pion mange [f e5d6] au passage. Légal ou pas ? [q 3 Légal_ou_pas_?]
[m exd6# mat] [z d6e7 1.45 2.6] [x impact] Mat. Légal !
Tu le savais ? Oui ou non ?""",
},
"pigeon_en_1": {
    "cote": "noirs",
    "hook": "If he eats your candy,|he's mated.",
    "voix": """[mischievously] If he eats your candy, he's mated.
You're Black. You leave a pawn alone. His pony eats it, then another, hitting your queen and your rook.
Your queen eats two pawns, check. He hides behind his bishop. Your pony jumps. [laughs] Mate.
Would you fall for it? Yes or no?""",
    "script": """[p e4 e5 Nf3 Nc6 Bc4 Nd4 Nxe5 Qg5 Nxf7 Qxg2 Rf1 Qxe4+ Be2 Nf3#] [s tag f3 3.0 MATE] If he eats your candy, he's mated.
[h] [p e4 e5 Nf3 Nc6 Bc4] You're Black. You leave [m Nd4 bizarre] a pawn alone. [s bonbon e5 2.5] His pony [m Nxe5 gaffe] eats it, [s tag e5 2.0 PIGEON] [m Qg5] then [m Nxf7] another, hitting [f f7g5 f7h8] your queen and your rook.
Your queen [m Qxg2] eats two [m Rf1] pawns, [m Qxe4+] check. He hides [m Be2] behind his bishop. Your pony [m Nf3# mat] [z f3e1 1.45 2.6] [x impact] jumps. Mate.
Would you fall for it? Yes or no?""",
},
"pigeon_en_2": {
    "cote": "noirs",
    "hook": "If he eats your pony,|he's mated.",
    "voix": """[mischievously] If he eats your pony, he's mated.
You're Black. You park your pony next to his king. His pigeon pawn chases it. You push a pawn.
He eats your pony: the biggest candy ever. You take back. A highway opens. Your queen dives. [laughs] Mate.
Would you fall for it? Yes or no?""",
    "script": """[p e4 e5 Nf3 Nc6 Bb5 Nf6 O-O Ng4 h3 h5 hxg4 hxg4 Ne1 Qh4 f3 g3 d4 Qh2#] [s tag h2 3.0 MATE] If he eats your pony, he's mated.
[h] [p e4 e5 Nf3 Nc6 Bb5 Nf6 O-O] You're Black. You park [m Ng4 bizarre] your pony next to his king. His pigeon pawn [m h3] chases it. You push [m h5 brillant] a pawn.
He eats [m hxg4 gaffe] your pony: [s tag g4 2.5 PIGEON] the biggest candy ever. You take [m hxg4] back. A highway [m Ne1] opens. [f h8h2] Your queen [m Qh4] dives. [m f3] [m g3] [m d4] [m Qh2# mat] [z h2 1.45 2.6] [x impact] Mate.
Would you fall for it? Yes or no?""",
},
})
QUESTIONS.update({
    "pigeon_jour_3": "A = oui · B = jamais.|Commente !",
    "pigeon_jour_4": "Suis le compte|pour la suite",
    "quiz_legal_3_long": "Tu le savais ?|Oui ou non ?",
    "quiz_legal_3_court": "Tu le savais ?|Oui ou non ?",
    "pigeon_en_1": "Would you fall for it?|Yes or no?",
    "pigeon_en_2": "Would you fall for it?|Yes or no?",
})

# ---------- file du 24-25/10 (scénariste) : T1-fin (pigeon_jour #5 A Caro-Kann, #6 B Hollandais), T6-durée paire 2 (Opéra long/court, sans voix), T7-langue (pigeon_en #3-#4) ----------
# Producteur (25/10, 1 h) : coups vérifiés python-chess + Stockfish 19 (WASM) : 3 mats confirmés (Nd6#, Qh5#, Rd8#) ; gaffes Ngf6 et gxh4 = mat en 1.
# 1re phrase réécrite pour s'adresser à « tu » (règle du producteur) ; « veut la bloquer » retiré (inexact : Ngf6 ne bloque pas la dame).
CARO_PIEGE = "e4 c6 d4 d5 Nc3 dxe4 Nxe4 Nd7 Qe2 Ngf6"          # + Nd6#
DUTCH_PIEGE = "d4 f5 Bg5 h6 Bh4 g5 e3"                          # + gxh4 Qh5#
OPERA_FIN = OPERA + " Nxb5 cxb5 Bxb5+ Nbd7 O-O-O Rd8 Rxd7 Rxd7 Rd1 Qe6 Bxd7+ Nxd7 Qb8+ Nxb8 Rd8#"
PERSO.update({
"pigeon_jour_5": {
    "cote": "blancs",
    "hook": "S'il sort ce poney,|tu le mates.",
    "voix": """[mischievously] S'il sort ce poney, tu le mates.
Tu as les Blancs. Il mange un pion, tu le reprends. Ta dame vise son roi. Le pigeon sort son autre poney. Erreur.
Ton poney saute devant son roi. [laughs] Mat étouffé.
Tu serais tombé dedans ? Commente A : oui, ou B : jamais.""",
    "script": """[p """ + CARO_PIEGE + """] [s tag f6 3.0 LE_PIGEON] S'il sort ce poney, tu le mates.
[h] [p e4 c6 d4 d5 Nc3] Tu as les Blancs. Il mange [m dxe4] un pion, tu le [m Nxe4] reprends. [m Nd7] Ta dame [m Qe2] [f e2e8] vise son roi. Le pigeon sort son autre [m Ngf6 gaffe] poney. [s tag f6 2.0 LE_PIGEON] Erreur.
Ton poney [m Nd6# mat] [z d6e8 1.45 2.6] [x impact] saute devant son roi. Mat étouffé.
Tu serais tombé dedans ? Commente A : oui, ou B : jamais.""",
},
"pigeon_jour_6": {
    "cote": "blancs",
    "hook": "S'il mange ton fou,|tu le mates en 5 coups.",
    "voix": """[mischievously] S'il mange ton fou, tu le mates en cinq coups.
Tu as les Blancs. Ton fou attaque. Le pigeon le chasse avec deux pions. Tu libères le chemin de ta dame. Il mange ton fou, le bonbon. Ta dame bondit. [laughs] Mat.
Tu serais tombé dedans ? Suis le compte pour la suite.""",
    "script": """[p """ + DUTCH_PIEGE + """] [s tag h4 3.0 LE_BONBON] S'il mange ton fou, tu le mates en cinq coups.
[h] [p d4 f5] Tu as les Blancs. Ton fou [m Bg5] attaque. Le pigeon le chasse [m h6] avec [m Bh4] deux [m g5] pions. Tu libères [m e3 brillant] le chemin [f d1h5] de ta dame. Il mange ton fou, [m gxh4 gaffe] [s tag h4 2.0 LE_PIGEON] le bonbon. Ta dame [m Qh5# mat] [z h5e8 1.45 2.6] [x impact] bondit. Mat.
Tu serais tombé dedans ? Suis le compte pour la suite.""",
},
"analyse_celebre_2_long": {   # SANS VOIX (commande "muet") : sous-titres en phrases + musique ; vraie partie de 1858, aucun nom de joueur
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Tu joues pendant l'opéra ?|Mat en 17 coups.",
    "voix": """Tu joues pendant l'opéra ? Mat en 17 coups.
Paris, 1858. Tu as les Blancs. Le pigeon a deux conseillers.
Tes pièces sortent vite. Ta dame gagne du temps.
Ta dame attaque deux choses d'un coup.
Il se défend. Puis il rate un détail : il pousse un pion.
Tu donnes ton poney. Le bonbon. Il le mange.
Ton fou donne échec. Son poney se met en travers.
Tu roques loin. Et tu donnes une tour.
Il la mange. Sa dame se range.
Ton fou donne échec. Il le mange.
Puis… ta dame. Le plus gros bonbon du monde.
Il la mange. Trois… deux… un…
Ta tour. Mat.
Tu l'avais vu ? Oui ou non ?""",
    "script": """[p """ + OPERA_FIN + """] [s tag d8 3.0 MAT] Tu joues pendant l'opéra ? Mat en 17 coups.
[h] [p] Paris, 1858. Tu as les Blancs. Le pigeon a deux conseillers.
Tes [m e4] pièces [m e5] sortent [m Nf3] vite. [m d6] Ta [m d4] dame [m Bg4] gagne [m dxe5] du [m Bxf3] temps.
[m Qxf3] Ta [m dxe5] dame [m Bc4] attaque [m Nf6] deux [m Qb3] [f b3b7 b3f7] choses d'un coup.
Il se [m Qe7] défend. Puis [m Nc3] il rate [m c6] un [m Bg5] détail : il pousse [m b5 erreur] un pion.
Tu donnes [m Nxb5 brillant] ton poney. [s bonbon b5 2.5] Le bonbon. Il le [m cxb5] mange.
Ton fou donne [m Bxb5+] échec. Son poney se met [m Nbd7] en travers.
Tu roques [m O-O-O] loin. [m Rd8] Et tu donnes [m Rxd7 brillant] une tour.
Il la [m Rxd7] mange. [m Rd1] Sa dame [m Qe6] se range.
Ton fou donne [m Bxd7+] échec. Il le [m Nxd7] mange.
Puis… [m Qb8+ brillant] ta dame. [s bonbon b8 2.5] Le plus gros bonbon du monde.
Il la [m Nxb8 gaffe] mange. Trois… deux… un…
Ta tour. [m Rd8# mat] [z d8e8 1.45 2.6] [x impact] Mat.
Tu l'avais vu ? Oui ou non ?""",
},
"analyse_celebre_2_court": {  # SANS VOIX : même partie, sans explication ni rebondissement intermédiaire
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Tu joues pendant l'opéra ?|Mat en 17 coups.",
    "voix": """Tu joues pendant l'opéra ? Mat en 17 coups.
Tu as les Blancs. Tu donnes un poney.
Puis une tour. Il mange tout.
Puis ta dame. Le plus gros bonbon.
Mat.
Tu l'avais vu ? Oui ou non ?""",
    "script": """[p """ + OPERA_FIN + """] [s tag d8 3.0 MAT] Tu joues pendant l'opéra ? Mat en 17 coups.
[h] [p """ + OPERA + """] Tu as les Blancs. Tu donnes [m Nxb5 brillant] un [m cxb5] poney.
[m Bxb5+] Puis [m Nbd7] une [m O-O-O] tour. [m Rd8] Il [m Rxd7 brillant] mange [m Rxd7] tout. [m Rd1] [m Qe6]
[m Bxd7+] Puis [m Nxd7] ta [m Qb8+ brillant] dame. Le plus [m Nxb8 gaffe] gros bonbon.
[m Rd8# mat] [z d8e8 1.45 2.6] [x impact] Mat.
Tu l'avais vu ? Oui ou non ?""",
},
"pigeon_en_3": {
    "cote": "blancs",
    "hook": "If he plays this pony,|you mate him.",
    "voix": """[mischievously] If he plays this pony, you mate him.
You're White. He eats a pawn, you take it back. Your queen eyes his king. The pigeon brings out his other pony. Big mistake.
Your pony jumps in front of his king. [laughs] Smothered mate.
Would you fall for it? Comment A: yes, or B: never.""",
    "script": """[p """ + CARO_PIEGE + """] [s tag f6 3.0 PIGEON] If he plays this pony, you mate him.
[h] [p e4 c6 d4 d5 Nc3] You're White. He eats [m dxe4] a pawn, you take it [m Nxe4] back. [m Nd7] Your queen [m Qe2] [f e2e8] eyes his king. The pigeon brings out his other [m Ngf6 gaffe] pony. [s tag f6 2.0 PIGEON] Big mistake.
Your pony [m Nd6# mat] [z d6e8 1.45 2.6] [x impact] jumps in front of his king. Smothered mate.
Would you fall for it? Comment A: yes, or B: never.""",
},
"pigeon_en_4": {
    "cote": "blancs",
    "hook": "If he eats your bishop,|you mate him in five.",
    "voix": """[mischievously] If he eats your bishop, you mate him in five.
You're White. Your bishop attacks. The pigeon chases it with two pawns. You open the road for your queen. He eats your bishop, the candy. Your queen leaps across the board. [laughs] Mate.
Would you fall for it? Follow for the next trap.""",
    "script": """[p """ + DUTCH_PIEGE + """] [s tag h4 3.0 CANDY] If he eats your bishop, you mate him in five.
[h] [p d4 f5] You're White. Your bishop [m Bg5] attacks. The pigeon chases it [m h6] with [m Bh4] two [m g5] pawns. You open [m e3 brillant] the road [f d1h5] for your queen. He eats your bishop, [m gxh4 gaffe] [s tag h4 2.0 PIGEON] the candy. Your queen [m Qh5# mat] [z h5e8 1.45 2.6] [x impact] leaps across the board. Mate.
Would you fall for it? Follow for the next trap.""",
},
})
QUESTIONS.update({
    "pigeon_jour_5": "A = oui · B = jamais.|Commente !",
    "pigeon_jour_6": "Suis le compte|pour la suite",
    "analyse_celebre_2_long": "Tu l'avais vu ?|Oui ou non ?",
    "analyse_celebre_2_court": "Tu l'avais vu ?|Oui ou non ?",
    "pigeon_en_3": "A = yes · B = never.|Comment!",
    "pigeon_en_4": "Follow for|the next trap",
})

# ---------- file du 25-26/10 (scénariste) : T1-fin (pigeon_jour #7 A Philidor, #8 B Boden), T6-durée paire 3 (quiz « tour clouée » long/court, sans voix), T7-langue (pigeon_en #5-#6) ----------
# Producteur (26/10, 1 h) : coups vérifiés python-chess + Stockfish 19 (WASM) : 4...Be7 = +2,6 ; 7...gxh6 = mat en 1 (8.Qxf7#) ; 14.Bxd5 = mat en 2 (Qxc3+ bxc3 Ba3#) ; quiz : Rxe8# (6 coups de tour légaux).
# Hook #8 « mat en trois » remplacé par « il est mat » (après 13...d5 le mat n'est pas forcé : seul 14.Bxd5 le permet) ; même phrase en EN.
PHILIDOR_PIEGE = "e4 e5 Nf3 d6 d4 Nd7 Bc4 Be7 dxe5 dxe5 Qd5"       # + Nh6 Bxh6 gxh6 Qxf7#
CLOUEE = "fen:4r1k1/5ppp/8/8/8/8/4R3/4K3_w_-_-_0_1"                 # + Rxe8#
PERSO.update({
"pigeon_jour_7": {
    "cote": "blancs",
    "hook": "S'il sort ce fou,|ta dame menace le mat.",
    "voix": """[mischievously] S'il sort ce fou, ta dame menace le mat.
Tu as les Blancs. Le pigeon sort son fou. Tu échanges les pions, ta dame fonce au centre. Elle vise le point faible de son roi. Il défend avec un poney. Tu le manges. S'il reprend, [laughs] c'est mat.
Tu serais tombé dedans ? Commente A : oui, ou B : jamais.""",
    "script": """[p """ + PHILIDOR_PIEGE + """] [f d5f7 c4f7] [s tag f7 3.0 MENACE] S'il sort ce fou, ta dame menace le mat.
[h] [p e4 e5 Nf3 d6 d4 Nd7 Bc4] Tu as les Blancs. Le pigeon sort [m Be7 gaffe] son fou. [s tag e7 2.0 LE_PIGEON] Tu échanges [m dxe5] les [m dxe5] pions, ta dame [m Qd5 brillant] fonce au centre. Elle vise [f d5f7 c4f7] le point faible de son roi. Il défend avec [m Nh6] un poney. Tu le [m Bxh6] manges. S'il [m gxh6 gaffe] reprend, c'est [m Qxf7# mat] [z f7e8 1.45 2.6] [x impact] mat.
Tu serais tombé dedans ? Commente A : oui, ou B : jamais.""",
},
"pigeon_jour_8": {
    "cote": "noirs",
    "hook": "Donne ta dame au pigeon :|il est mat.",
    "voix": """[mischievously] Donne ta dame au pigeon : il est mat.
Tu as les Noirs. Le pigeon fait le grand roque. Tu avances un pion, il le mange. Tu offres ta dame, le plus gros bonbon du monde. Il la mange. Tes deux fous se croisent. [laughs] Mat.
Tu serais tombé dedans ? Suis le compte pour la suite.""",
    "script": """[p """ + BODEN + """ O-O-O d5 Bxd5 Qxc3+] [s bonbon c3 3.0] Donne ta dame au pigeon : il est mat.
[h] [p """ + BODEN + """] Tu as les Noirs. Le pigeon fait [m O-O-O] le grand roque. Tu avances [m d5 brillant] un pion, il le [m Bxd5 gaffe] mange. [s tag d5 2.0 LE_PIGEON] Tu offres [m Qxc3+ brillant] ta dame, [s bonbon c3 2.5] le plus gros bonbon du monde. Il la [m bxc3 gaffe] mange. Tes deux fous [f f5b1 f8a3] se croisent. [m Ba3# mat] [z a3c1 1.45 2.6] [x impact] Mat.
Tu serais tombé dedans ? Suis le compte pour la suite.""",
},
"quiz_legal_4_long": {   # SANS VOIX (commande "muet") : sous-titres en phrases + musique
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Ta tour est clouée,|mais elle fait mat. Légal ?",
    "voix": """Ta tour est clouée, mais elle fait mat. Légal ?
Tu as les Blancs. Le pigeon cloue ta tour sur ton roi.
Une tour clouée ne peut pas sauter de côté.
Vers la gauche ? Illégal. Vers la droite ? Illégal.
Mais sur la colonne, elle a le droit.
Six coups légaux. Un seul est le bon.
Un de ces coups mange la tour du pigeon. Légal ou pas ?
Son roi est enfermé par ses propres pions.
Tour prend tour. Mat. LÉGAL !
Tu le savais ? Oui ou non ?""",
    "script": """[p """ + CLOUEE + """] [f e2e8] [s tag e8 3.0 LE_PIGEON] Ta tour est clouée, mais elle fait mat. Légal ?
[h] Tu as les Blancs. Le pigeon [f e8e1] cloue ta tour sur ton roi. [s tag e8 2.5 LE_PIGEON]
Une tour clouée ne peut pas sauter de côté. [z e2 1.3 2.0]
Vers la gauche ? [f e2a2] [s tag a2 2.0 ILLEGAL] Illégal. Vers la droite ? [f e2h2] [s tag h2 2.0 ILLEGAL] Illégal.
Mais sur la colonne, [f e2e7] elle a le droit.
Six coups légaux. [s tag e5 2.5 6_COUPS] Un seul est le bon.
Un de ces coups [f e2e8] mange la tour du pigeon. Légal ou pas ? [q 3 Légal_ou_pas_?]
Son roi est enfermé [z g7 1.3 2.0] par ses propres pions.
Tour prend tour. [m Rxe8# mat] [z e8g8 1.45 2.6] [x impact] Mat. LÉGAL !
Tu le savais ? Oui ou non ?""",
},
"quiz_legal_4_court": {  # SANS VOIX : même position, sans essais illégaux ni compteur
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Ta tour est clouée,|mais elle fait mat. Légal ?",
    "voix": """Ta tour est clouée, mais elle fait mat. Légal ?
Ton roi est derrière ta tour. Le pigeon la cloue.
Elle ne peut pas sortir de la colonne… mais elle peut la suivre. Légal ou pas ?
Tour prend tour. Mat. Légal !
Tu le savais ? Oui ou non ?""",
    "script": """[p """ + CLOUEE + """] [f e2e8] [s tag e8 3.0 LE_PIGEON] Ta tour est clouée, mais elle fait mat. Légal ?
[h] Ton roi est derrière ta tour. Le pigeon [f e8e1] la cloue. [z e2 1.3 2.0]
Elle ne peut pas sortir de la colonne… mais elle peut [f e2e8] la suivre. Légal ou pas ? [q 3 Légal_ou_pas_?]
Tour prend tour. [m Rxe8# mat] [z e8g8 1.45 2.6] [x impact] Mat. Légal !
Tu le savais ? Oui ou non ?""",
},
"pigeon_en_5": {
    "cote": "blancs",
    "hook": "If he plays this bishop,|your queen threatens mate.",
    "voix": """[mischievously] If he plays this bishop, your queen threatens mate.
You're White. You trade pawns and your queen jumps to the center, eyeing his weak spot. He defends with a pony. You take it. If he takes back, [laughs] it's mate.
Would you fall for it? Comment A: yes, or B: never.""",
    "script": """[p """ + PHILIDOR_PIEGE + """] [f d5f7 c4f7] [s tag f7 3.0 THREAT] If he plays this bishop, your queen threatens mate.
[h] [p e4 e5 Nf3 d6 d4 Nd7 Bc4] You're [m Be7 gaffe] White. [s tag e7 2.0 PIGEON] You trade [m dxe5] pawns [m dxe5] and your queen [m Qd5 brillant] jumps to the center, eyeing [f d5f7 c4f7] his weak spot. He defends with [m Nh6] a pony. You [m Bxh6] take it. If he [m gxh6 gaffe] takes back, it's [m Qxf7# mat] [z f7e8 1.45 2.6] [x impact] mate.
Would you fall for it? Comment A: yes, or B: never.""",
},
"pigeon_en_6": {
    "cote": "noirs",
    "hook": "Give your queen to the pigeon:|he's mated.",
    "voix": """[mischievously] Give your queen to the pigeon: he's mated.
You're Black. The pigeon castles long. You push a pawn, he eats it. You offer your queen, the biggest candy in the world. He eats it. Your two bishops cross. [laughs] Mate.
Would you fall for it? Follow for the next trap.""",
    "script": """[p """ + BODEN + """ O-O-O d5 Bxd5 Qxc3+] [s bonbon c3 3.0] Give your queen to the pigeon: he's mated.
[h] [p """ + BODEN + """] You're Black. The pigeon castles [m O-O-O] long. You push [m d5 brillant] a pawn, he [m Bxd5 gaffe] eats it. [s tag d5 2.0 PIGEON] You offer [m Qxc3+ brillant] your queen, [s bonbon c3 2.5] the biggest candy in the world. He [m bxc3 gaffe] eats it. Your two bishops [f f5b1 f8a3] cross. [m Ba3# mat] [z a3c1 1.45 2.6] [x impact] Mate.
Would you fall for it? Follow for the next trap.""",
},
})
QUESTIONS.update({
    "pigeon_jour_7": "A = oui · B = jamais.|Commente !",
    "pigeon_jour_8": "Suis le compte|pour la suite",
    "quiz_legal_4_long": "Tu le savais ?|Oui ou non ?",
    "quiz_legal_4_court": "Tu le savais ?|Oui ou non ?",
    "pigeon_en_5": "A = yes · B = never.|Comment!",
    "pigeon_en_6": "Follow for|the next trap",
})

# ---------- file du 26-27/10 (scénariste) : 2 FR + 4 EN. T1-fin (Owen = B, Traxler = A, seed 2710262233), T7-5/T7-6, T6-4 EN (ANALYSE « Game of the Century », sans voix) ----------
# Producteur (27/10, 1 h) : python-chess + Stockfish 19 (WASM) : Owen 3...f5 = +3,5, 6...Nf6 = mat en 2, 7...Nxh5 8.Bg6# ;
# Traxler 7.Kg1 = 0,0 puis 8.Nxh8 = mat en 1 (Qf2#) ; partie de 1956 : 41 coups légaux, 41...Rc2# mat, 17...Be6 = -2,9, 18.Bxb6 = -7,1.
OWEN_PIEGE = "e4 b6 d4 Bb7 Bd3 f5 exf5 Bxg2 Qh5+ g6 fxg6 Nf6 gxh7 Nxh5"        # + Bg6#
TRAXLER_PIEGE = "e4 e5 Nf3 Nc6 Bc4 Nf6 Ng5 Bc5 Nxf7 Bxf2+ Kxf2 Nxe4+ Kg1 Qh4"  # + Nxh8 Qf2#
GOTC = ("Nf3 Nf6 c4 g6 Nc3 Bg7 d4 O-O Bf4 d5 Qb3 dxc4 Qxc4 c6 e4 Nbd7 Rd1 Nb6 Qc5 Bg4 Bg5 Na4 Qa3 Nxc3 bxc3 Nxe4 "
        "Bxe7 Qb6 Bc4 Nxc3 Bc5 Rfe8+ Kf1 Be6 Bxb6 Bxc4+ Kg1 Ne2+ Kf1 Nxd4+ Kg1 Ne2+ Kf1 Nc3+ Kg1 axb6 Qb4 Ra4 Qxb6 Nxd1 "
        "h3 Rxa2 Kh2 Nxf2 Re1 Rxe1 Qd8+ Bf8 Nxe1 Bd5 Nf3 Ne4 Qb8 b5 h4 h5 Ne5 Kg7 Kg1 Bc5+ Kf1 Ng3+ Ke1 Bb4+ Kd1 Bb3+ "
        "Kc1 Ne2+ Kb1 Nc3+ Kc1 Rc2#")
_G = GOTC.split()
GOTC_12 = " ".join(_G[:23])   # jusqu'à 12.Qa3
GOTC_17 = " ".join(_G[:34])   # jusqu'à 17...Be6 (image 1)
GOTC_35 = " ".join(_G[:69])   # jusqu'à 35.Kg1
GOTC_41 = " ".join(_G[:81])   # jusqu'à 41.Kc1
PERSO.update({
"pigeon_en_7": {
    "cote": "blancs",
    "hook": "Lose your queen,|then mate with a bishop.",
    "voix": """[mischievously] Lose your queen, then mate with a bishop.
You're White. The pigeon eats a candy on your side. Your queen jumps out with check. You push pawns, he must block. He eats your queen with a pony. Your bishop slides in. [laughs] Mate.
Would you fall for it? Follow for the next trap.""",
    "script": """[p """ + OWEN_PIEGE + """] [f d3g6] [s tag g6 3.0 MATE] Lose your queen, then mate with a bishop.
[h] [p e4 b6 d4 Bb7 Bd3 f5] You're [m exf5] White. The pigeon eats [m Bxg2] a candy [s bonbon g2 2.0] on your side. Your queen [m Qh5+ brillant] jumps out with check. [m g6] You push [m fxg6] pawns, he must [m Nf6 gaffe] block. [m gxh7 brillant] He eats your queen [m Nxh5] [s tag h5 2.0 PIGEON] with a pony. Your bishop [m Bg6# mat] [z g6e8 1.45 2.6] [x impact] slides in. Mate.
Would you fall for it? Follow for the next trap.""",
},
"pigeon_jour_9": {
    "cote": "blancs",
    "hook": "Perds ta dame,|mate avec ton fou.",
    "voix": """[mischievously] Perds ta dame, mate avec ton fou.
Tu as les Blancs. Le pigeon mange un bonbon chez toi. Ta dame sort avec échec. Tu pousses tes pions, il doit parer. Il mange ta dame avec un poney. Ton fou glisse. [laughs] Mat.
Tu serais tombé dedans ? Suis le compte pour la suite.""",
    "script": """[p """ + OWEN_PIEGE + """] [f d3g6] [s tag g6 3.0 MAT] Perds ta dame, mate avec ton fou.
[h] [p e4 b6 d4 Bb7 Bd3 f5] Tu as [m exf5] les Blancs. Le pigeon mange [m Bxg2] un bonbon [s bonbon g2 2.0] chez toi. Ta dame [m Qh5+ brillant] sort avec échec. [m g6] Tu pousses [m fxg6] tes pions, il doit [m Nf6 gaffe] parer. [m gxh7 brillant] Il mange ta dame [m Nxh5] [s tag h5 2.0 LE_PIGEON] avec un poney. Ton fou [m Bg6# mat] [z g6e8 1.45 2.6] [x impact] glisse. Mat.
Tu serais tombé dedans ? Suis le compte pour la suite.""",
},
"pigeon_en_8": {
    "cote": "noirs",
    "hook": "He eats your rook,|and you mate him.",
    "voix": """[mischievously] He eats your rook, and you mate him.
You're Black. The pigeon grabs a candy. You give him your bishop, he eats it. Your pony strikes with check. Your queen leaps out. He eats your rook. [laughs] Mate.
Would you fall for it? Comment A: yes, or B: never.""",
    "script": """[p """ + TRAXLER_PIEGE + """] [f h4f2] [s tag f2 3.0 MATE] He eats your rook, and you mate him.
[h] [p e4 e5 Nf3 Nc6 Bc4 Nf6 Ng5 Bc5] You're Black. The pigeon grabs [m Nxf7] a candy. [s bonbon f7 2.0] You give him [m Bxf2+ brillant] your bishop, he [m Kxf2] eats it. Your pony [m Nxe4+] strikes with check. [m Kg1] Your queen [m Qh4 brillant] leaps out. He eats [m Nxh8 gaffe] [s tag h8 2.0 PIGEON] your rook. [m Qf2# mat] [z f2g1 1.45 2.6] [x impact] Mate.
Would you fall for it? Comment A: yes, or B: never.""",
},
"pigeon_jour_10": {
    "cote": "noirs",
    "hook": "Il mange ta tour,|et tu lui mets mat.",
    "voix": """[mischievously] Il mange ta tour, et tu lui mets mat.
Tu as les Noirs. Le pigeon prend un bonbon. Tu lui offres ton fou, il le mange. Ton poney attaque avec échec. Ta dame sort. Il mange ta tour. [laughs] Mat.
Tu serais tombé dedans ? Commente A : oui, ou B : jamais.""",
    "script": """[p """ + TRAXLER_PIEGE + """] [f h4f2] [s tag f2 3.0 MAT] Il mange ta tour, et tu lui mets mat.
[h] [p e4 e5 Nf3 Nc6 Bc4 Nf6 Ng5 Bc5] Tu as les Noirs. Le pigeon prend [m Nxf7] un bonbon. [s bonbon f7 2.0] Tu lui offres [m Bxf2+ brillant] ton fou, il le [m Kxf2] mange. Ton poney [m Nxe4+] attaque avec échec. [m Kg1] Ta dame [m Qh4 brillant] sort. Il mange [m Nxh8 gaffe] [s tag h8 2.0 LE_PIGEON] ta tour. [m Qf2# mat] [z f2g1 1.45 2.6] [x impact] Mat.
Tu serais tombé dedans ? Commente A : oui, ou B : jamais.""",
},
"analyse_celebre_3_court": {  # SANS VOIX (commande "muet") ; vraie partie de 1956, aucun nom de joueur ; T6-4 variante B
    "cote": "noirs", "sous_titres": "phrase",
    "hook": "A 13-year-old gives|his queen away. And wins.",
    "voix": """A 13-year-old gives his queen away. And wins.
White takes his queen. He lets it go.
Check! And check. And check. His pony will not stop.
Queen gone? Black now has more material.
16 moves later… MATE.
Would you have seen it? Yes or no?""",
    "script": """[p """ + GOTC_17 + """] [s tag b6 3.0 QUEEN] A 13-year-old gives his queen away. And wins.
[h] [p """ + GOTC_17 + """] White takes [m Bxb6] his queen. [s tag b6 2.0 GONE] He lets it go.
[m Bxc4+ brillant] Check! [m Kg1] And [m Ne2+] check. [m Kf1] And [m Nxd4+] check. [m Kg1] His [m Ne2+] pony [m Kf1] will [m Nc3+] not [m Kg1] stop.
Queen gone? [m axb6] Black [m Qb4] now [m Ra4] has [m Qxb6] more [m Nxd1 brillant] material.
[p """ + GOTC_41 + """] 16 moves later… [m Rc2# mat] [z c2c1 1.45 2.6] [x impact] MATE.
Would you have seen it? Yes or no?""",
},
"analyse_celebre_3_long": {   # SANS VOIX (commande "muet") ; même partie ; T6-4 variante A (61-75 s)
    "cote": "noirs", "sous_titres": "phrase",
    "hook": "A 13-year-old gives|his queen away. And wins.",
    "voix": """A 13-year-old gives his queen away. And wins.
White has just won a pawn. He is a grown-up. Black is 13.
Black's queen is hanging. He ignores it.
White's bishop takes the queen. Then… check.
Again: check. Again: check. Again: check. And check.
His pony hits the rook. The queen is gone, but Black has more material.
White still has the queen. But no way out.
His king runs. And runs. Left. Left. Left. Trapped.
MATE.
Would you have seen it? Yes or no?""",
    "script": """[p """ + GOTC_17 + """] [s tag b6 3.0 QUEEN] A 13-year-old gives his queen away. And wins.
[h] [p """ + GOTC_12 + """] [m Nxc3] White [m bxc3] has [m Nxe4] just [m Bxe7] won a pawn. He [m Qb6] is [m Bc4] a [m Nxc3] grown-up. [m Bc5] Black [m Rfe8+] is [m Kf1] 13. [m Be6]
Black's queen [z b6 1.3 2.0] [s tag b6 2.5 HANGING] is hanging. He ignores it.
White's bishop [m Bxb6] takes the queen. Then… [m Bxc4+ brillant] check.
[m Kg1] Again: [m Ne2+] check. [m Kf1] Again: [m Nxd4+] check. [m Kg1] Again: [m Ne2+] check. [m Kf1] And [m Nc3+] check. [m Kg1]
[m axb6] His pony [m Qb4] hits [m Ra4] the [m Qxb6] rook. [m Nxd1 brillant] The queen is gone, but Black has more material.
[m h3] White [m Rxa2] still [m Kh2] has [m Nxf2] the [m Re1] queen. [m Rxe1] But [m Qd8+] no [m Bf8] way [m Nxe1] out.
[p """ + GOTC_35 + """] His [m Bc5+] king [m Kf1] runs. [m Ng3+] And [m Ke1] runs. [m Bb4+] Left. [m Kd1] [m Bb3+] Left. [m Kc1] [m Ne2+] Left. [m Kb1] [m Nc3+] Trapped. [m Kc1]
[m Rc2# mat] [z c2c1 1.45 2.6] [x impact] MATE.
Would you have seen it? Yes or no?""",
},
})
QUESTIONS.update({
    "pigeon_en_7": "Follow for|the next trap",
    "pigeon_jour_9": "Suis le compte|pour la suite",
    "pigeon_en_8": "A = yes · B = never.|Comment!",
    "pigeon_jour_10": "A = oui · B = jamais.|Commente !",
    "analyse_celebre_3_court": "Would you have|seen it? Yes or no?",
    "analyse_celebre_3_long": "Would you have|seen it? Yes or no?",
})

# ---------- file du 27-28/10 (scénariste) : 2 FR + 4 EN. T1-fin (Vienne = A, Italienne = B, seed 2810262233), T7-7/T7-8, T6-5 EN (quiz « prise en passant clouée », avec voix) ----------
# Producteur (28/10, 1 h) : python-chess + Stockfish 19 (WASM, prof. 16) : Vienne 4...Nxc3?? = mat en 1 (5.Qxf7#), 4...Nd6 était le coup ;
# Italienne 3...Qf6 = +1,1 pour les Blancs, 4.Nxe5?? = mat en 1 (4...Qxf2#) ; quiz : b5xc6 e.p. pseudo-légal mais illégal (tour h5 sur la 5e rangée), coups légaux Kb6 Ka6 Ka4 b6.
# Aucune musique (décision de Simon du 27/10) : "sans_musique": true dans toutes les commandes. Image 1 = position finale (boucle ouverte) + étiquette REWIND.
VIENNE_PIEGE = "e4 e5 Nc3 Nf6 Bc4 Nxe4 Qh5 Nxc3"          # + Qxf7#
ITALIENNE_PIEGE = "e4 e5 Nf3 Bc5 Bc4 Qf6 Nxe5"            # + Qxf2#
EPC_AVANT = "fen:7k/2p5/8/KP5r/8/8/8/8_b_-_-_0_1"          # le pigeon joue c5
EPC_QUIZ = "fen:7k/8/8/KPp4r/8/8/8/8_w_-_c6_0_2"           # bxc6 e.p. ? illégal
EPC_SI = "fen:7k/8/2P5/K6r/8/8/8/8_b_-_-_0_2"              # si on prenait : la tour voit le roi
PERSO.update({
"pigeon_en_9": {
    "cote": "blancs",
    "hook": "He eats your pony.|Then you checkmate him.",
    "voix": """[mischievously] He eats your pony. Then you checkmate him.
You're White. The pigeon grabs a candy. Your queen sneaks out. Greedy pigeon eats your pony too. Your queen takes the last candy. [laughs] Mate.
Would you fall for it? Comment A: yes, or B: never.""",
    "script": """[p """ + VIENNE_PIEGE + """ Qxf7#] [s tag f7 1.0 REWIND] He eats your pony. Then you checkmate him.
[h] [p e4 e5 Nc3 Nf6 Bc4] You're White. The pigeon grabs [m Nxe4 gaffe] a candy. [s bonbon e4 2.0] Your queen [m Qh5 brillant] sneaks out. Greedy pigeon [m Nxc3 gaffe] eats your pony [s tag c3 2.0 PIGEON] too. Your queen takes [m Qxf7# mat] [z f7e8 1.45 2.6] [x impact] the last candy. Mate.
Would you fall for it? Comment A: yes, or B: never.""",
},
"pigeon_jour_11": {
    "cote": "blancs",
    "hook": "Il mange ton poney.|Puis tu lui mets mat.",
    "voix": """[mischievously] Il mange ton poney. Puis tu lui mets mat.
Tu as les Blancs. Le pigeon prend un bonbon. Ta dame sort en douce. Gourmand, il mange aussi ton poney. Ta dame prend le dernier bonbon. [laughs] Mat.
Tu serais tombé dedans ? Commente A : oui, ou B : jamais.""",
    "script": """[p """ + VIENNE_PIEGE + """ Qxf7#] [s tag f7 1.0 REWIND] Il mange ton poney. Puis tu lui mets mat.
[h] [p e4 e5 Nc3 Nf6 Bc4] Tu as les Blancs. Le pigeon prend [m Nxe4 gaffe] un bonbon. [s bonbon e4 2.0] Ta dame [m Qh5 brillant] sort en douce. Gourmand, il mange [m Nxc3 gaffe] aussi ton poney. [s tag c3 2.0 LE_PIGEON] Ta dame prend [m Qxf7# mat] [z f7e8 1.45 2.6] [x impact] le dernier bonbon. Mat.
Tu serais tombé dedans ? Commente A : oui, ou B : jamais.""",
},
"pigeon_en_10": {
    "cote": "noirs",
    "hook": "He eats a free pawn.|You mate him.",
    "voix": """[mischievously] He eats a free pawn. You mate him.
You're Black. Your bishop eyes his weak spot. Your queen steps out. The pigeon sees a free pawn and grabs it with his pony. Greedy. Your queen eats the candy in front of his king. [laughs] Mate.
Would you fall for it? Follow for the next trap.""",
    "script": """[p """ + ITALIENNE_PIEGE + """ Qxf2#] [s tag f2 1.0 REWIND] He eats a free pawn. You mate him.
[h] [p e4 e5 Nf3] You're Black. Your bishop [m Bc5 brillant] eyes [f c5f2] his weak spot. [m Bc4] Your queen [m Qf6 brillant] steps out. The pigeon sees a free pawn and grabs it [m Nxe5 gaffe] with his pony. [s tag e5 2.0 PIGEON] Greedy. Your queen eats [m Qxf2# mat] [z f2e1 1.45 2.6] [x impact] the candy in front of his king. Mate.
Would you fall for it? Follow for the next trap.""",
},
"pigeon_jour_12": {
    "cote": "noirs",
    "hook": "Il mange un pion gratuit.|Tu lui mets mat.",
    "voix": """[mischievously] Il mange un pion gratuit. Tu lui mets mat.
Tu as les Noirs. Ton fou vise sa faille. Ta dame sort. Le pigeon voit un pion gratuit et le prend avec son poney. Gourmand. Ta dame mange le bonbon devant son roi. [laughs] Mat.
Tu serais tombé dedans ? Suis le compte pour la suite.""",
    "script": """[p """ + ITALIENNE_PIEGE + """ Qxf2#] [s tag f2 1.0 REWIND] Il mange un pion gratuit. Tu lui mets mat.
[h] [p e4 e5 Nf3] Tu as les Noirs. Ton fou [m Bc5 brillant] vise [f c5f2] sa faille. [m Bc4] Ta dame [m Qf6 brillant] sort. Le pigeon voit un pion gratuit et le prend [m Nxe5 gaffe] avec son poney. [s tag e5 2.0 LE_PIGEON] Gourmand. Ta dame mange [m Qxf2# mat] [z f2e1 1.45 2.6] [x impact] le bonbon devant son roi. Mat.
Tu serais tombé dedans ? Suis le compte pour la suite.""",
},
"quiz_legal_5_court": {   # AVEC VOIX ; T6-5 variante B (30-45 s), pause chrono 2 s
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "This capture is illegal.|Can you see why?",
    "voix": """This capture is illegal. Can you see why?
The pigeon jumps his pawn right next to yours. You can take it in passing. Tempting! Legal or illegal? Decide before the timer ends.
Illegal! Both pawns vanish and his rook hits your king.
Would you have taken it? Yes or no?""",
    "script": """[p """ + EPC_QUIZ + """] [f b5c6] [s tag c6 3.0 WHY] This capture is illegal. Can you see why?
[h] [p """ + EPC_AVANT + """] The pigeon jumps [m c5] his pawn right next to yours. [s tag c5 2.0 PIGEON] You can take it [f b5c6] in passing. Tempting! Legal or illegal? Decide before the timer ends. [q 2 Legal_or_illegal?]
Illegal! [p """ + EPC_SI + """] Both pawns vanish and his rook [f h5a5] [z a5 1.3 2.0] [x impact] hits your king.
Would you have taken it? Yes or no?""",
},
"quiz_legal_5_long": {    # AVEC VOIX LONGUE (≈ 700 car., élargissement de Simon du 27/10) ; T6-5 variante A (61-75 s), pause chrono 2 s
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "This capture is illegal.|Can you see why?",
    "voix": """This capture is illegal. Can you see why?
You're White. Your king hides on the edge, right behind your pawn. Far away on the same row, the pigeon's rook is waiting.
Suddenly the pigeon jumps his pawn two steps, right next to yours. A special capture appears, just for this one turn. Tempting! You can take the candy in passing.
But wait. Look along the row. Your king. Your pawn. His pawn. His rook. Legal or illegal? Decide before the timer ends.
Illegal! If you take, both pawns vanish. The road opens. The rook hits your king. You can never leave your king in check.
So you walk your king away, or push your pawn ahead. The candy stays on the plate. Next time, look at the whole row.
Would you have taken it? Yes or no?""",
    "script": """[p """ + EPC_QUIZ + """] [f b5c6] [s tag c6 3.0 WHY] This capture is illegal. Can you see why?
[h] [p """ + EPC_AVANT + """] You're White. Your king [z a5 1.3 2.0] hides on the edge, right behind your pawn. Far away on the same row, the pigeon's rook [s tag h5 2.5 PIGEON] is waiting.
Suddenly the pigeon jumps [m c5] his pawn two steps, right next to yours. A special capture [f b5c6] appears, just for this one turn. Tempting! You can take the candy [s bonbon c5 2.5] in passing.
But wait. Look along the row. Your king. [z a5 1.3 1.5] Your pawn. [z b5 1.3 1.5] His pawn. [z c5 1.3 1.5] His rook. [z h5 1.3 1.5] Legal or illegal? Decide before the timer ends. [q 2 Legal_or_illegal?]
Illegal! If you take, [p """ + EPC_SI + """] both pawns vanish. The road opens. [f h5a5] The rook hits your king. [x impact] [s tag a5 2.5 CHECK] You can never leave your king in check.
[p """ + EPC_QUIZ + """] So you walk your king away, [f a5a4 a5b6] or push your pawn ahead. [f b5b6] The candy stays on the plate. Next time, look at the whole row. [f a5h5]
Would you have taken it? Yes or no?""",
},
})
QUESTIONS.update({
    "pigeon_en_9": "A = yes · B = never.|Comment!",
    "pigeon_jour_11": "A = oui · B = jamais.|Commente !",
    "pigeon_en_10": "Follow for|the next trap",
    "pigeon_jour_12": "Suis le compte|pour la suite",
    "quiz_legal_5_court": "Would you have|taken it? Yes or no?",
    "quiz_legal_5_long": "Would you have|taken it? Yes or no?",
})

# ---------- file du 28-29/10 (scénariste) : 4 EN + 2 FR. T11-série (Kieninger = A « Chess Trap #1 », Légal = B isolée), T13-fin-quiz (#6 FR = B, #7 FR = A), seed 2910262233 ----------
# Producteur (29/10, 1 h) : python-chess + Stockfish 17 natif (1,5 s) : Légal 5.Nxe5 = meilleur coup (+1,9), 5...Bxd1?? = mat en 2 ; Kieninger 8.axb4?? = mat en 1 (8.Nxe5 = +0,4) ;
# quiz #6 : O-O légal, roi pas en échec ; quiz #7 : Kxd3 illégal (fou f5 cloué mais protège), seule prise Rxf5+ (+6,6). Aucune musique. Décompte silencieux de 2 s ([q 2]) à la place de « three, two, one » dit.
LEGAL_AVANT = "e4 e5 Nf3 d6 Bc4 Bg4 Nc3 g6"
KIENINGER_AVANT = "d4 Nf6 c4 e5 dxe5 Ng4 Bf4 Nc6 Nf3 Bb4+ Nbd2 Qe7 a3 Ngxe5"
ROQUE_ECHEC = "e4 d5 exd5 Qxd5 Nc3"
FOU_CLOUE = "fen:5k2/6pp/8/5b2/8/3pK3/6PP/5R2_w_-_-_0_1"
PERSO.update({
"pigeon_en_11": {   # Légal, T11-série B (isolée : ni numéro ni teaser)
    "cote": "blancs",
    "hook": "Give your queen.|Win.",
    "voix": """[mischievously] He eats your queen. Smile. Your bishop checks. His king steps aside. Your pony jumps in. [laughs] Mate.""",
    "script": """[p """ + LEGAL_AVANT + """] He [m Nxe5 brillant] eats [m Bxd1 gaffe] your queen. [s tag d1 1.5 PIGEON] [h] Smile. Your bishop [m Bxf7+ brillant] checks. His king [m Ke7] steps aside. Your pony [m Nd5# mat] [z d5e7 1.45 2.6] [x impact] jumps in. Mate.""",
},
"pigeon_en_12": {   # Kieninger, T11-série A (« Chess Trap #1 » + teaser final)
    "cote": "noirs",
    "hook": "Chess Trap #1|He eats your bishop. You mate.",
    "voix": """[mischievously] He eats your bishop. You mate. You give a pawn. Your bishop checks. Your queen steps out. He takes the bishop. Your pony jumps. [laughs] Mate.""",
    "script": """[p """ + KIENINGER_AVANT + """] He eats [m axb4 gaffe] your bishop. You [m Nd3# mat] [x impact] mate. [h] [p d4 Nf6 c4] You give [m e5 brillant] a pawn. [m dxe5] Your [p d4 Nf6 c4 e5 dxe5 Ng4 Bf4 Nc6 Nf3] bishop [m Bb4+ brillant] checks. [m Nbd2] Your queen [m Qe7] steps [m a3] out. [m Ngxe5] He takes [m axb4 gaffe] the bishop. [s tag b4 2.0 PIGEON] Your pony [m Nd3# mat] [z d3e1 1.45 2.6] [x impact] jumps. Mate.""",
},
"quiz_legal_6_en": {   # roque après un échec, EN, sans test, renvoi vers le site
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Your king was in check.|Can you castle?",
    "voix": """Your king was in check. Can you castle? The queen checked your king. You blocked it. Now she is gone. Legal or illegal?
Legal! Only a check right now stops you. Find your own mistakes, free: blundercheck dot app.""",
    "script": """[p """ + ROQUE_ECHEC + """] Your king [m Qe5+ gaffe] [f e5e1] was in check. Can you castle? [h] The queen checked [f e5e1] your king. You [m Be2] blocked [m Nf6] it. [m Nf3] Now she [m Qa5] is gone. Legal or illegal? [q 2 Legal_or_illegal?]
Legal! [m O-O brillant] [x impact] Only a check right now stops you. Find your own mistakes, free: blundercheck dot app.""",
},
"quiz_legal_6_fr": {   # roque après un échec, FR, T13-fin-quiz B (fin nette)
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Ton roi a pris un échec.|Tu peux roquer ?",
    "voix": """Ton roi a pris un échec. Tu peux roquer ? La dame noire t'a mis en échec. Tu as bloqué. Maintenant elle est partie. Légal ou pas ?
Légal ! Seul un échec en ce moment t'en empêche.""",
    "script": """[p """ + ROQUE_ECHEC + """] Ton roi [m Qe5+ gaffe] [f e5e1] a pris un échec. Tu peux roquer ? [h] La dame noire [f e5e1] t'a mis en échec. Tu [m Be2] as bloqué. [m Nf6] Maintenant [m Nf3] elle [m Qa5] est partie. Légal ou pas ? [q 2 Légal_ou_pas_?]
Légal ! [m O-O brillant] [x impact] Seul un échec en ce moment t'en empêche.""",
},
"quiz_legal_7_fr": {   # fou cloué, FR, T13-fin-quiz A (question finale)
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Ton roi peut manger|ce pion ?",
    "voix": """Ton roi peut manger ce pion ? Un fou noir le protège. Mais ta tour le cloue. Légal ou pas ?
Illégal ! Un fou cloué protège toujours. Prends-le avec ta tour. Tu le savais ? Oui ou non ?""",
    "script": """[p """ + FOU_CLOUE + """] [f e3d3] Ton roi peut manger ce pion ? [h] Un fou noir [f f5d3] le protège. Mais ta tour [f f1f8] le cloue. Légal ou pas ? [q 2 Légal_ou_pas_?]
Illégal ! [s tag d3 2.0 NON] [x impact] Un fou cloué protège toujours. Prends-le [m Rxf5+ brillant] avec ta tour. Tu le savais ? Oui ou non ?""",
},
"quiz_legal_7_en": {   # fou cloué, EN (E2' : remplace prof_corrige), renvoi vers le site
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Can your king|take this pawn?",
    "voix": """Can your king take this pawn? A black bishop guards it. But your rook pins it. Legal or illegal?
Illegal! A pinned bishop still guards. Take it with your rook. Analyze your own games, free: blundercheck dot app.""",
    "script": """[p """ + FOU_CLOUE + """] [f e3d3] Can your king take this pawn? [h] A black bishop [f f5d3] guards it. But your rook [f f1f8] pins it. Legal or illegal? [q 2 Legal_or_illegal?]
Illegal! [s tag d3 2.0 NO] [x impact] A pinned bishop still guards. Take it [m Rxf5+ brillant] with your rook. Analyze your own games, free: blundercheck dot app.""",
},
})
QUESTIONS.update({
    "pigeon_en_11": None,                                  # B : fin en boucle, sans texte
    "pigeon_en_12": "Trap #2 tomorrow|Follow",             # A : teaser de série
    "quiz_legal_6_en": "Analyze your own game, free|blundercheck.app/try",
    "quiz_legal_6_fr": None,                               # T13 B : fin nette
    "quiz_legal_7_fr": "Tu le savais ?|Oui ou non ?",      # T13 A
    "quiz_legal_7_en": "Analyze your own games, free|blundercheck.app/try",
})

# ---------- file du 29-30/10 (scénariste 22 h 33) : 3 EN + 2 FR. T11-série (Sicilienne = A « Chess Trap #2 », Scandinave = B), T13-fin-quiz B (pat) ----------
# Producteur (30/10, 1 h) : python-chess + Stockfish 17.1 (WASM, 0,7 s) : Sicilienne 10.Bxf6?? = mat (10.Qd2 +3,2) ; Scandinave 7...Nxd1?? = mat en 1 (7...Qd6/Qd4 gagnent) ;
# Alekhine 9...h6?? = mat en 2 (9...Qe8) ; quiz pat : Qg6 = pat, Qg8# = mat. Aucune musique. Anti-doublon : NOUVEAU pour les 4 positions.
SICI_AVANT = "e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nf6 Nc3 Qc7 Bg5 Nc6 Ndb5 Qb6 Bf4 e5 Bg5 Bc5"
SCAN_AVANT = "e4 d5 exd5 Nf6 Bb5+ Bd7 Bc4 Bg4 Nf3 Nxd5 Nc3"
ALEK_AVANT = "e4 Nf6 e5 Nd5 d4 d6 Nf3 Bf5 Bc4 Nb6 Bxf7+ Kxf7 Ng5+ Kg8 e6 Bg6 Qf3"
MAT_PAT = "fen:7k/5K2/8/6Q1/8/8/8/8_w_-_-_0_1"
PERSO.update({
"pigeon_en_13": {   # Sicilienne, T11-série A (« Chess Trap #2 », badge permanent)
    "cote": "noirs", "serie": "Chess Trap #2",
    "hook": "He took the knight.|Big mistake.",
    "voix": """[mischievously] White takes your knight and smiles. He thinks he is winning. Now give him a bishop for free. It takes a pawn, with check. The king must run away. Then your queen jumps in. Checkmate! One small gift, and his king is lost. Trap #3 tomorrow. Follow!""",
    "script": """[p """ + SICI_AVANT + """] White [m Bxf6 gaffe] takes your knight and smiles. [h] He thinks [s tag f6 2.0 PIGEON] he is winning. Now give him a bishop [z c5f2 1.3 2.0] for free. It takes [m Bxf2+ brillant] a pawn, with check. The king must [m Kd2] run away. Then your queen [m Qe3# mat] [z e3d2 1.45 2.6] [x impact] jumps in. Checkmate! One small gift, and his king is lost. Trap #3 tomorrow. Follow!""",
},
"pigeon_en_14": {   # Scandinave, T11-série B (sans badge ni numéro) ; 30/10 : 19,1 s → pause 2 s « Find the mate! » (voix réutilisée, 0 crédit)
    "cote": "blancs",
    "hook": "Ignore the knight.|Jump forward.",
    "voix": """[mischievously] He took your knight. Do not take it back! Stay calm and jump your other knight forward. Now your queen is hanging, but his king is not safe. He eats the giant candy. Your bishop takes the pawn. Checkmate! Follow: one new trap every day.""",
    "script": """[p """ + SCAN_AVANT + """] He [m Nxc3] took your knight. [h] Do not take [f b2c3] it back! Stay calm and jump your other knight [m Ne5 brillant] [z e5 1.3 2.0] forward. Now your queen [f c3d1] is hanging, but his king is not safe. He eats [m Nxd1 gaffe] [s tag d1 2.0 PIGEON] the giant candy. [q 2 Find_the_mate!] Your bishop takes [m Bxf7# mat] [z f7e8 1.45 2.6] [x impact] the pawn. Checkmate! Follow: one new trap every day.""",
},
"pigeon_en_15": {   # Alekhine, sans test
    "cote": "blancs",
    "hook": "Sacrifice the queen.|Pawn mates.",
    "voix": """[mischievously] Your knight is under attack. Ignore it! Give him your queen, with check. He thinks he is safe. He has to take it. Now push your pawn. The pawn gives checkmate! It sounds crazy, but it works. A tiny pawn beats the king. Follow: one new trap every day.""",
    "script": """[p """ + ALEK_AVANT + """] Your knight [m h6 gaffe] [f h6g5] is under attack. [h] Ignore it! Give him your queen, [m Qf7+ brillant] [z f7 1.3 2.0] with check. He thinks he is safe. He has [m Bxf7] to take it. Now push your pawn. The pawn [m exf7# mat] [z f7g8 1.45 2.6] [x impact] gives checkmate! It sounds crazy, but it works. A tiny pawn beats the king. Follow: one new trap every day.""",
},
"pigeon_jour_13": {   # Scandinave FR (jumeau de pigeon_en_14), sans test
    "cote": "blancs",
    "hook": "Ne reprends pas|le cavalier !",
    "voix": """[mischievously] Il a pris ton cavalier. Ne reprends pas ! Reste calme. Saute avec l'autre cavalier. Ta dame est attaquée, mais son roi est en danger. Le pigeon croque le gros bonbon. Ton fou prend le pion : échec et mat ! Abonne-toi : un piège par jour.""",
    "script": """[p """ + SCAN_AVANT + """] Il a [m Nxc3] pris ton cavalier. [h] Ne reprends [f b2c3] pas ! Reste calme. Saute avec l'autre [m Ne5 brillant] [z e5 1.3 2.0] cavalier. Ta dame [f c3d1] est attaquée, mais son roi est en danger. Le pigeon croque [m Nxd1 gaffe] [s tag d1 2.0 LE_PIGEON] le gros bonbon. Ton fou prend [m Bxf7# mat] [z f7e8 1.45 2.6] [x impact] le pion : échec et mat ! Abonne-toi : un piège par jour.""",
},
"quiz_legal_8_fr": {   # mat ou pat, FR, T13-fin-quiz B (fin nette, appel seul)
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Mat ou pat ?",
    "voix": """Ton roi et ta dame contre le roi seul. Tu joues la dame ici. C'est mat ? Non ! Le roi noir ne peut plus bouger, mais il n'est pas attaqué : c'est pat, nulle ! Ça arrive à tout le monde. Le vrai mat, c'était la dame au bord. Abonne-toi : un piège par jour.""",
    "script": """[p """ + MAT_PAT + """] [f g5g6] Ton roi et ta dame contre le roi seul. [h] Tu joues [m Qg6] la dame ici. C'est mat ? [q 2 Mat_ou_pat_?] Non ! [s tag h8 2.0 PAT] [x impact] Le roi noir ne peut plus bouger, mais il n'est pas attaqué : c'est pat, nulle ! Ça arrive à tout le monde. Le vrai mat, [p """ + MAT_PAT + """] c'était la dame [m Qg8# mat] [z g8h8 1.45 2.6] au bord. Abonne-toi : un piège par jour.""",
},
})
QUESTIONS.update({
    "pigeon_en_13": "Trap #3 tomorrow|Follow!",
    "pigeon_en_14": "Follow: one new|trap every day",
    "pigeon_en_15": "Follow: one new|trap every day",
    "pigeon_jour_13": "Abonne-toi :|un piège par jour",
    "quiz_legal_8_fr": "Abonne-toi :|un piège par jour",
})

# ---------- file du 30-31/10 (scénariste 22 h 33) : 3 EN + 2 FR (+ version longue T6 TikTok EN). Niveau 1300-2000 ----------
# Producteur (31/10, 1 h) : python-chess + Stockfish 19 (WASM, 0,5 s) : Zukertort 9...Nxd4?? = mat en 2 (9...f6 tient) ;
# Caro-Kann 12...Be7?? = mat en 2 (12...Qe7) ; double échec : Qxf3 illégal, seuls Kf1/Ke2/Kf2. Anti-doublon : NOUVEAU (3 positions). Aucune musique.
ZUK_AVANT = "Nf3 g6 d4 Bg7 c4 d6 Nc3 e5 e4 exd4 Bg5 Ne7 Nd5 Nbc6 Nxd4 Bxd4"
CARO_AVANT = "e4 c6 Nc3 d5 Nf3 dxe4 Nxe4 Nf6 Ng3 h5 h4 Bg4 Be2 Nbd7 Ng5 Bxe2 Qxe2 e6"
CARO_FIN = CARO_AVANT + " Nf5 g6 Nxe6 fxe6 Qxe6+"
DOUBLE_ECHEC = "fen:4k3/8/8/8/1b6/8/3n4/3QK3_b_-_-_0_1"
PERSO.update({
"gourmande_en_1": {   # Halloween, la Gourmande déguisée, Zukertort (réserve n° 5, 1770), sans test
    "cote": "blancs",
    "hook": "She eats your queen.|Then mate.",
    "voix": """[mischievously] Happy Halloween! The Greedy One is in costume, but she still loves candy. Your queen takes the bishop: free candy for her! Her knight gobbles your queen. Now your knight jumps with check. Her king has only one square. Your bishop slides in: checkmate! Her dark bishop was gone, so her king had no defender. Follow: one new trap every day.""",
    "script": """[p """ + ZUK_AVANT + """ Qxd4] Happy [m Nxd4 gaffe] Halloween! [h] The Greedy One is in costume, [p """ + ZUK_AVANT + """] but she still loves candy. Your queen [m Qxd4 brillant] takes the bishop: free candy for her! Her knight [m Nxd4 gaffe] [s tag d4 2.0 PIGEON] gobbles your queen. Now your knight [m Nf6+ brillant] [z f6 1.3 2.0] jumps with check. Her king [m Kf8] has only one square. Your bishop [m Bh6# mat] [z h6f8 1.45 2.6] [x impact] slides in: checkmate! Her dark bishop was gone, so her king had no defender. Follow: one new trap every day.""",
},
"gourmande_fr_1": {   # jumeau FR de gourmande_en_1, sans test
    "cote": "blancs",
    "hook": "Elle mange ta dame.|Puis mat.",
    "voix": """[mischievously] Joyeux Halloween ! La Gourmande est déguisée, mais elle adore toujours les bonbons. Ta dame prend le fou : bonbon gratuit pour elle ! Son cavalier avale ta dame. Ton cavalier saute avec échec. Son roi n'a qu'une seule case. Ton fou arrive : échec et mat ! Son fou des cases noires était parti, son roi n'avait plus de défenseur. Abonne-toi : un piège par jour.""",
    "script": """[p """ + ZUK_AVANT + """ Qxd4] Joyeux [m Nxd4 gaffe] Halloween ! [h] La Gourmande est déguisée, [p """ + ZUK_AVANT + """] mais elle adore toujours les bonbons. Ta dame [m Qxd4 brillant] prend le fou : bonbon gratuit pour elle ! Son cavalier [m Nxd4 gaffe] [s tag d4 2.0 LE_PIGEON] avale ta dame. Ton cavalier [m Nf6+ brillant] [z f6 1.3 2.0] saute avec échec. Son roi [m Kf8] n'a qu'une seule case. Ton fou [m Bh6# mat] [z h6f8 1.45 2.6] [x impact] arrive : échec et mat ! Son fou des cases noires était parti, son roi n'avait plus de défenseur. Abonne-toi : un piège par jour.""",
},
"pigeon_en_16": {   # Caro-Kann Two Knights (réserve n° 9, 1592), T11-série B (sans badge ni numéro) ; remplace Scotch
    "cote": "blancs",
    "hook": "Knight sacrifice.|Then mate.",
    "voix": """[mischievously] He blocks the check with his bishop. Big mistake! Rewind. Your knight jumps forward. Your other knight crashes in and offers itself. The pigeon takes it. Your queen takes back, with check. He blocks with the bishop. Now your first knight jumps with check. His king steps aside. Your queen delivers the mate. Remember: a sacrifice opens the road to the king. Follow: one new trap every day.""",
    "script": """[p """ + CARO_FIN + """] He blocks [m Be7 gaffe] the check with his bishop. Big mistake! [h] Rewind. [p """ + CARO_AVANT + """] Your knight [m Nf5] jumps forward. [m g6] Your other knight [m Nxe6 brillant] crashes in and offers itself. The pigeon [m fxe6] [s tag e6 2.0 PIGEON] takes it. Your queen [m Qxe6+ brillant] takes back, with check. He blocks [m Be7 gaffe] with the bishop. Now your first knight [m Nd6+ brillant] [z d6 1.3 2.0] jumps with check. His king [m Kf8] steps aside. Your queen [m Qf7# mat] [z f7f8 1.45 2.6] [x impact] delivers the mate. Remember: a sacrifice opens the road to the king. Follow: one new trap every day.""",
},
"quiz_legal_9_en": {   # double échec, EN, T6-durée B (court)
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Check twice.|Take the knight?",
    "voix": """Your king is in check from a knight and a bishop at the same time. Your queen can take the knight. Is it legal? Think! The answer is no. Even without the knight, the bishop still gives check. In a double check, only the king can move. Follow: one new rule every day.""",
    "script": """[p """ + DOUBLE_ECHEC + """] [m Nf3+ gaffe] Your king is in check [f f3e1] from a knight and a bishop at the same time. [h] Your queen [f d1f3] can take the knight. Is it legal? Think! [q 2 Legal_or_illegal?] The answer is no. [s tag f3 2.0 NO] [x impact] Even without the knight, the bishop [f b4e1] still gives check. In a double check, only the king [m Kf2 brillant] can move. Follow: one new rule every day.""",
},
"quiz_legal_9_fr": {   # double échec, FR, T13-fin-quiz A (question finale)
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Double échec :|tu prends ?",
    "voix": """Ton roi est en échec par un cavalier et un fou en même temps. Ta dame peut prendre le cavalier. C'est légal ? Réfléchis ! Réponse : non. Même sans le cavalier, le fou donne toujours échec. En double échec, seul le roi peut bouger. Tu le savais ? Abonne-toi : une règle par jour.""",
    "script": """[p """ + DOUBLE_ECHEC + """] [m Nf3+ gaffe] Ton roi est en échec [f f3e1] par un cavalier et un fou en même temps. [h] Ta dame [f d1f3] peut prendre le cavalier. C'est légal ? Réfléchis ! [q 2 Légal_ou_pas_?] Réponse : non. [s tag f3 2.0 NON] [x impact] Même sans le cavalier, le fou [f b4e1] donne toujours échec. En double échec, seul le roi [m Kf2 brillant] peut bouger. Tu le savais ? Abonne-toi : une règle par jour.""",
},
})
PERSO["quiz_legal_9_en_long"] = dict(PERSO["quiz_legal_9_en"],   # T6-durée A (TikTok EN seulement) : même voix (0 crédit), pause 6 s
    script=PERSO["quiz_legal_9_en"]["script"].replace("[q 2 Legal_or_illegal?]", "[q 6 Legal_or_illegal?_Think!]"))
QUESTIONS.update({
    "gourmande_en_1": "Follow: one new|trap every day",
    "gourmande_fr_1": "Abonne-toi :|un piège par jour",
    "pigeon_en_16": "Follow: one new|trap every day",
    "quiz_legal_9_en": "Follow: one new|rule every day",
    "quiz_legal_9_en_long": "Follow: one new|rule every day",
    "quiz_legal_9_fr": "Tu le savais ?|Abonne-toi",
})

# ---------- file du 31/10-1/11 (scénariste 22 h 33) : 4 EN + 2 FR. T11-série (e.p. = A « Chess Trap #3 », dragon accéléré = B), T13-fin-quiz B ----------
# Producteur (1/11, 1 h) : python-chess + Stockfish 17.1 (WASM lite, 0,5 s) : dragon accéléré 9...d5?? +3,6 (9...Nxe4 -1,3), 10.Bc5 meilleur ;
# Défense russe 5...c5?? +3,1 (5...d5 0), 6.Qa4+ meilleur, 7.Qxe4+ ; e.p. : 1...c5+ 2.bxc6+ légal et échec ; grand roque légal (case voisine de la tour attaquée, route du roi libre).
# Textes : dragon « Take the knight… » corrigé (c'est la dame noire qui prend le cavalier) ; russe « ouvre la diagonale » corrigé (la diagonale était déjà ouverte). Anti-doublon : NOUVEAU (4 positions). Aucune musique.
EP_ECHEC = "fen:8/1rpkb3/8/1P6/1N1K4/8/8/8_b_-_-_0_1"
DRAGON_AVANT = "e4 c5 Nc3 Nc6 Nf3 g6 d4 cxd4 Nxd4 Bg7 Be3 Nf6 Bc4 Qb6 Nb3 Qb4 Bd3"
GRAND_ROQUE = "fen:r3k2r/ppp2ppp/2n2nb1/8/8/2N2N2/PP3PPP/R3K2R_w_KQkq_-_0_1"
RUSSE_AVANT = "e4 e5 Nf3 Nf6 Nxe5 d6 Nf3"
PERSO.update({
"quiz_legal_10_en": {   # prise en passant qui pare un échec, T11-série A (« Chess Trap #3 », badge permanent)
    "cote": "blancs", "sous_titres": "phrase", "serie": "Chess Trap #3",
    "hook": "Check!|Can you take en passant?",
    "voix": """A pawn jumps two squares and checks your king. Can you capture it en passant? Yes! Your pawn lands with check and forks the king and the rook. The king runs, you win the rook. En passant can answer a check. Trap #4 tomorrow. Follow!""",
    "script": """[p """ + EP_ECHEC + """] A pawn [m c5+ gaffe] [f c5d4] jumps two squares and checks your king. [h] Can you capture it en passant? [q 2 En_passant?] Yes! Your pawn [m bxc6+ brillant] [z c6 1.3 2.0] [x impact] lands with check and forks the king and the rook. [f c6b7] The king [m Kd6] runs, you win [m cxb7 brillant] [z b7 1.45 2.6] the rook. En passant can answer a check. Trap #4 tomorrow. Follow!""",
},
"quiz_legal_10_fr": {   # jumeau FR, T13-fin-quiz B (fin nette, appel seul)
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Échec !|Prise en passant ?",
    "voix": """Son pion avance de deux cases et te met en échec. Peux-tu le prendre en passant ? Oui ! Ton pion arrive avec échec et vise la tour. Le roi fuit, tu gagnes la tour. La prise en passant peut parer un échec. Abonne-toi : un piège par jour pour monter ton Elo.""",
    "script": """[p """ + EP_ECHEC + """] Son pion [m c5+ gaffe] [f c5d4] avance de deux cases et te met en échec. [h] Peux-tu le prendre en passant ? [q 2 En_passant_?] Oui ! Ton pion [m bxc6+ brillant] [z c6 1.3 2.0] [x impact] arrive avec échec et vise la tour. [f c6b7] Le roi [m Kd6] fuit, tu gagnes [m cxb7 brillant] [z b7 1.45 2.6] la tour. La prise en passant peut parer un échec. Abonne-toi : un piège par jour pour monter ton Elo.""",
},
"pigeon_en_17": {   # 1/11 : 18,0 s → pause 3 s « Find the trap! » (voix réutilisée, 0 crédit) ; Sicilienne dragon accéléré (réserve n° 1, 1693), dame piégée, T11-série B (sans badge ni numéro)
    "cote": "blancs",
    "hook": "His queen|has no escape.",
    "voix": """[mischievously] His queen wandered far from home. One bishop move hits it, and every escape square loses. Her best try takes a knight. You take back and win the queen. Always check where your queen can run. Follow: one new trap every day.""",
    "script": """[p """ + DRAGON_AVANT + """] His queen [m d5 gaffe] wandered far from home. [h] [q 3 Find_the_trap!] One bishop move [m Bc5 brillant] [z c5b4 1.3 2.0] hits it, [s tag b4 2.0 TRAPPED] and every escape square loses. Her best try [m Qxc3+] takes a knight. You take back [m bxc3 brillant] [z c3 1.45 2.6] [x impact] and win the queen. Always check where your queen can run. Follow: one new trap every day.""",
},
"quiz_legal_11_en": {   # grand roque, case voisine de la tour attaquée, sans test
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Castle long.|Legal?",
    "voix": """His bishop hits the square next to your rook. Can you castle long? Yes! Only the king's path must be safe. The king crosses two squares, and neither is attacked. The rook can cross an attacked square. Follow: one new puzzle every day.""",
    "script": """[p """ + GRAND_ROQUE + """] [f g6b1] His bishop hits the square next to your rook. [h] Can you castle long? [q 2 Legal_or_illegal?] Yes! [m O-O-O brillant] [z c1 1.3 2.0] [x impact] Only the king's path must be safe. The king crosses two squares, and neither is attacked. The rook can cross an attacked square. Follow: one new puzzle every day.""",
},
"pigeon_jour_14": {   # Défense russe (réserve n° 3, 1307), fourchette de dame, sans test
    "cote": "blancs",
    "hook": "Un échec,|deux cibles.",
    "voix": """[mischievously] Il croque ton pion avec son poney. Tu joues un petit coup tranquille. Il pousse un pion, mais la diagonale de son roi est grande ouverte. Ta dame sort : échec, et son poney est visé aussi. Tu gagnes le poney. Abonne-toi : un piège par jour pour monter ton Elo.""",
    "script": """[p """ + RUSSE_AVANT + """] Il croque [m Nxe4] ton pion avec son poney. [h] Tu joues [m c3] un petit coup tranquille. Il pousse [m c5 gaffe] un pion, mais la diagonale de son roi est grande ouverte. Ta dame [m Qa4+ brillant] [z a4 1.3 2.0] sort : échec, [m Nc6] et son poney [f a4e4] est visé aussi. Tu gagnes [m Qxe4+ brillant] [z e4 1.45 2.6] [x impact] le poney. Abonne-toi : un piège par jour pour monter ton Elo.""",
},
})
QUESTIONS.update({
    "quiz_legal_10_en": "Trap #4 tomorrow|Follow!",
    "quiz_legal_10_fr": "Abonne-toi :|un piège par jour",
    "pigeon_en_17": "Follow: one new|trap every day",
    "quiz_legal_11_en": "Follow: one new|puzzle every day",
    "pigeon_jour_14": "Abonne-toi :|un piège par jour",
})

# ---- 2/11 (Producteur, nuit du 1 au 2/11) : file du Scénariste, cases jamais dites (règle de l'univers) ----
NEUF_DAMES = "fen:R6R/3Q4/1Q4Q1/4Q3/2Q4Q/Q4Q2/pp1Q4/kBNN1KB1_w_-_-_0_1"
CARRE = "fen:8/8/5k2/8/1P6/8/8/7K_b_-_-_0_1"
SCHLIEMANN_AVANT = "fen:r1b1qrk1/ppp3pp/2pb1n2/4N1B1/3Pp3/2N5/PPP2PPP/R2Q1RK1_w_-_-_5_10"
CLOUAGE_AVANT = "fen:rnbqk2r/ppp2pbp/5np1/4p1B1/4P3/2N5/PPPQ1PPP/R3KBNR_w_KQkq_-_0_7"
PERSO.update({
"nb_coups_1": {   # 9 dames, 218 coups légaux (python-chess), position composée ; T14 A, T15-putaclic
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "9 queens.|How many moves?",
    "voix": """Nine queens on one board. How many legal moves for White? Fifty? A hundred? It's two hundred and eighteen! A composed position, not a real game. Follow: a new puzzle daily.""",
    "script": """[p """ + NEUF_DAMES + """] [f e5e8 e5h2 e5b8 e5a1] Nine queens on one board. [h] How many legal moves [f c4c8 c4f1 c4a2 c4g8] for White? Fifty? A hundred? [q 3 Count_them!] It's [s tag e5 4.0 218_MOVES] [x impact] two hundred and eighteen! A composed position, not a real game. Follow: a new puzzle daily.""",
},
"nb_coups_1_fr": {   # jumeau FR de nb_coups_1 ; T13 A (« Tu le savais ? »)
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "9 dames.|Combien de coups ?",
    "voix": """Neuf dames sur l'échiquier. Combien de coups légaux pour les Blancs ? Cinquante ? Cent ? Deux cent dix-huit ! Position inventée, pas une vraie partie. Tu le savais ? Abonne-toi : une énigme par jour.""",
    "script": """[p """ + NEUF_DAMES + """] [f e5e8 e5h2 e5b8 e5a1] Neuf dames sur l'échiquier. [h] Combien de coups légaux [f c4c8 c4f1 c4a2 c4g8] pour les Blancs ? Cinquante ? Cent ? [q 3 Compte-les !] [s tag e5 4.0 218_COUPS] [x impact] Deux cent dix-huit ! Position inventée, pas une vraie partie. Tu le savais ? Abonne-toi : une énigme par jour.""",
},
"finale_carre_1": {   # règle du carré ; Stockfish : 1…Re5/Re6/Rf5 nul, 1…Rg5 perd ; T14 B (Follow avant la révélation)
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Too far|to catch it?",
    "voix": """Can the king catch this pawn? Draw a square to the last row. The king is inside! Follow: one endgame trick a day. The king steps closer. The pawn runs, and the king follows. It runs again, the king follows again. One step from queening, and the king eats it.""",
    "script": """[p """ + CARRE + """] [f b4b8] Can the king catch this pawn? [h] Draw a square [f b4b8 b8f8 f8f4 f4b4] to the last row. The king is inside! [q 2 Inside?] Follow: one endgame trick a day. [m Ke5 brillant] The king steps closer. [m b5] The pawn runs, and the king [m Kd6] follows. It runs again, the king [p fen:8/8/5k2/8/1P6/8/8/7K_b_-_-_0_1 Ke5 b5 Kd6 b6 Kc6] follows again. [m b7] One step from queening, and the king [m Kxb7 brillant] [z b7 1.35 2.0] [x impact] eats it.""",
},
"finale_carre_1_fr": {   # jumeau FR de finale_carre_1
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Trop loin|pour le rattraper ?",
    "voix": """Le roi rattrape-t-il ce pion ? Dessine un carré jusqu'au bout. Le roi est dedans ! Le roi s'approche. Le pion court, le roi le suit. Il court encore, le roi suit encore. À un pas de la dame, le roi le croque. Abonne-toi : une astuce par jour.""",
    "script": """[p """ + CARRE + """] [f b4b8] Le roi rattrape-t-il ce pion ? [h] Dessine un carré [f b4b8 b8f8 f8f4 f4b4] jusqu'au bout. Le roi est dedans ! [q 2 Dedans ?] [m Ke5 brillant] Le roi s'approche. Le pion [m b5] court, le roi le suit. [p fen:8/8/5k2/8/1P6/8/8/7K_b_-_-_0_1 Ke5 b5 Kd6 b6 Kc6] Il court encore, le roi suit encore. À un [m b7] pas de la dame, le roi le [m Kxb7 brillant] [z b7 1.35 2.0] [x impact] croque. Abonne-toi : une astuce par jour.""",
},
"pigeon_en_18": {   # 2/11 18 h (demande de Simon) : vidéo complétée jusqu'à 13.Dxg4 Fxg4 ; texte de Simon (« only way » → « best try » : 13.Fh4/Ff4 parent aussi le mat, Stockfish)
    "cote": "noirs", "sous_titres": "phrase", "serie": "Chess Trap #4",
    "hook": "Your bishop is attacked.|Ignore it!",
    "voix": """White attacks your bishop. Ignore it! Bishop takes h2, check. King takes, knight g4, check. King back to g1. Now the queen goes to h5, threatening mate on h2. His best try: queen takes knight, bishop takes queen. White just lost his queen for a knight. Analyze your own game, free. Trap #5 tomorrow. Follow!""",
    "script": """[p fen:r1b1qrk1/ppp3pp/2pb1n2/6B1/2NPp3/2N5/PPP2PPP/R2Q1RK1_b_-_-_6_10] [f c4d6] White attacks your bishop. [h] Ignore it! [m Bxh2+ brillant] Bishop takes h2, check. [m Kxh2] King takes, knight g4, [m Ng4+] [z g4 1.3 2.0] check. King back to [m Kg1] g1. Now the queen goes to [m Qh5 brillant] h5, [f h5h2] threatening mate on h2. [q 1 Mate_threat!] His best try: [m Qxg4] queen takes knight, bishop takes [m Bxg4 brillant] [s tag g4 3.0 Queen_for_a_knight] [x impact] queen. White just lost his queen for a knight. Analyze your own game, free. Trap #5 tomorrow. Follow!""",
},
"tactique_clouage_1": {   # clouage : 7.Dxd8+ Rxd8 8.Cd5 h6 9.Fxf6+ Fxf6 10.Cxf6 (Stockfish +4,5) ; T14 B
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Trade queens.|Win a piece.",
    "voix": """Trade queens to win a piece? The king takes back. Now your knight jumps in. His knight is pinned, and attacked twice. He waits. Your bishop takes, check. His bishop takes back. Follow: a new trick daily. Knight takes: you win a piece!""",
    "script": """[p """ + CLOUAGE_AVANT + """] Trade [m Qxd8+] queens to win a piece? [h] The king [m Kxd8] takes back. Now your knight [m Nd5 brillant] [z d5 1.3 2.0] jumps in. His knight [f g5f6 d5f6] is pinned, and attacked twice. [m h6] He waits. Your bishop [m Bxf6+] takes, check. His bishop [m Bxf6] takes back. Follow: a new trick daily. Knight [m Nxf6 brillant] [z f6 1.4 2.4] [x impact] takes: you win a piece!""",
},
})
QUESTIONS.update({
    "nb_coups_1": "Follow: a new|puzzle daily",
    "nb_coups_1_fr": "Abonne-toi :|une énigme par jour",
    "finale_carre_1": "Follow: one endgame|trick a day",
    "finale_carre_1_fr": "Abonne-toi :|une astuce par jour",
    "pigeon_en_18": "Trap #5 tomorrow|Follow!",
    "tactique_clouage_1": "Follow: a new|trick daily",
})

# 3/11 (Producteur) : file du Scénariste du 2/11 ; coups vérifiés python-chess + Stockfish 16 (profondeur 20), aucune case dite
SAAVEDRA = "fen:8/8/1KP5/3r4/8/8/8/k7_w_-_-_0_1"
SAAVEDRA_CLE = "fen:8/2P5/8/8/3r4/8/2K5/k7_w_-_-_9_6"
TOUCHE = "fen:6k1/5ppp/2n5/8/8/8/5PPP/4R1K1_w_-_-_0_1"
PERSO.update({
"legende_miniature_1": {   # 1.d4 Nf6 2.Nd2 e5 3.dxe5 Ng4 4.h3?? Ne3 (−5,7) 5.fxe3 Qh4+ 6.g3 Qxg3# ; légende Gibaud–Lazard jamais prouvée (Winter) ; T14 B, T15
    "cote": "noirs", "sous_titres": "phrase",
    "hook": "Shortest game ever?|A myth!",
    "voix": """White pushes this pawn to chase the knight. Oops! The knight jumps in and forks the queen and the bishop. The shortest game ever? Legend says White resigned right here. Follow: one new trick a day. Take the knight, and the queen swings out with check. The king's only shield is a pawn. And then the queen simply takes it. Checkmate! Nobody ever proved this game was played. But the trap is real!""",
    "script": """[p d4 Nf6 Nd2 e5 dxe5 Ng4] White pushes [m h3 gaffe] this pawn to chase the knight. [h] Oops! The knight [m Ne3 brillant] [z e3 1.3 2.0] jumps in and forks [f e3d1 e3f1] the queen and the bishop. The shortest game ever? Legend says White resigned right here. [q 1 Legend?] Follow: one new trick a day. [m fxe3] Take the knight, and the queen swings out with [m Qh4+] check. The king's only shield is a [m g3] pawn. And then the queen simply [m Qxg3# mat] [z g3 1.35 2.0] [x impact] takes it. Checkmate! Nobody ever proved this game was played. But the trap is real!""",
},
"legende_miniature_1_fr": {   # jumeau FR de legende_miniature_1
    "cote": "noirs", "sous_titres": "phrase",
    "hook": "Plus courte partie ?|Un mythe !",
    "voix": """Les Blancs poussent ce pion pour chasser le cavalier. Aïe ! Le cavalier saute et attaque la dame et le fou en même temps. La partie la plus courte du monde ? La légende dit que les Blancs ont abandonné ici. S'ils prennent le cavalier, la dame sort avec échec. Le seul bouclier du roi, c'est un pion. Et la dame le croque tout simplement. Échec et mat ! Personne n'a jamais prouvé que cette partie a existé. Mais le piège est réel ! Abonne-toi : un piège par jour pour monter ton Elo.""",
    "script": """[p d4 Nf6 Nd2 e5 dxe5 Ng4] Les Blancs poussent [m h3 gaffe] ce pion pour chasser le cavalier. [h] Aïe ! Le cavalier [m Ne3 brillant] [z e3 1.3 2.0] saute et attaque [f e3d1 e3f1] la dame et le fou en même temps. La partie la plus courte du monde ? La légende dit que les Blancs ont abandonné ici. [q 1 Légende ?] [m fxe3] S'ils prennent le cavalier, la dame sort avec [m Qh4+] échec. Le seul bouclier du roi, c'est un [m g3] pion. Et la dame le croque [m Qxg3# mat] [z g3 1.35 2.0] [x impact] tout simplement. Échec et mat ! Personne n'a jamais prouvé que cette partie a existé. Mais le piège est réel ! Abonne-toi : un piège par jour pour monter ton Elo.""",
},
"touch_move_1": {   # règle FIDE art. 4.3 (pièce touchée) et 4.2 (j'adoube) ; Re8# mat en 1 ; coups du roi : Rf1, Rh1 (python-chess) ; position composée ; T14 A
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "You touched your king.|Can you still mate?",
    "voix": """Over the board, you touch your king on purpose. Then you spot mate in one with the rook. Can you still play it? No! Touched piece, moved piece. Your king has legal moves, so the king must move. If you had said "I adjust" before touching it, you would be free. Then the rook goes up: checkmate! Follow: one new rule a day.""",
    "script": """[p """ + TOUCHE + """] Over the board, you [s tag g1 2.5 TOUCHED] touch your king on purpose. [h] Then you spot [f e1e8] mate in one with the rook. Can you still play it? [q 2 Mate?] No! Touched piece, moved piece. Your king has legal moves, [f g1f1 g1h1] so the king must move. If you had said "I adjust" before touching it, you would be free. Then the rook goes up: [m Re8# mat] [z e8 1.3 2.0] [x impact] checkmate! Follow: one new rule a day.""",
},
"touch_move_1_fr": {   # jumeau FR de touch_move_1 ; T13 B (sans « Tu le savais ? »)
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Roi touché.|Mat quand même ?",
    "voix": """Sur un vrai échiquier, tu touches ton roi exprès. Puis tu vois un mat en un avec la tour. Peux-tu encore le jouer ? Non ! Pièce touchée, pièce jouée. Ton roi a des coups légaux, donc le roi doit bouger. Si tu avais dit « j'adoube » avant de le toucher, tu serais libre. Alors la tour monte : échec et mat ! Abonne-toi : une règle par jour.""",
    "script": """[p """ + TOUCHE + """] Sur un vrai échiquier, tu [s tag g1 2.5 TOUCHÉ] touches ton roi exprès. [h] Puis tu vois [f e1e8] un mat en un avec la tour. Peux-tu encore le jouer ? [q 2 Mat ?] Non ! Pièce touchée, pièce jouée. Ton roi a des coups légaux, [f g1f1 g1h1] donc le roi doit bouger. Si tu avais dit « j'adoube » avant de le toucher, tu serais libre. Alors la tour monte : [m Re8# mat] [z e8 1.3 2.0] [x impact] échec et mat ! Abonne-toi : une règle par jour.""",
},
"pigeon_en_19": {   # Russe : 5.c3 c5?? 6.Qa4+ Nc6 7.Qxe4+ (+4,0) ; coup juste 5…d5 (+0,1) ; réserve n° 3 (FR 1/11, jumeau EN) ; T11 A « Chess Trap #5 » ; vers /try
    "cote": "noirs", "sous_titres": "phrase", "serie": "Chess Trap #5",
    "hook": "White played a quiet move.|What's the threat?",
    "voix": """White just played a quiet pawn move. What does it threaten? The queen can jump out with check, and hit your knight at the same time. Push your other pawn? The queen checks from the side. You block with a knight. But look: now she simply grabs your other knight. A fork! Instead, push the center pawn: now the knight is guarded, and the trick fails. Analyze your own game, free. Trap #6 tomorrow. Follow!""",
    "script": """[p e4 e5 Nf3 Nf6 Nxe5 d6 Nf3 Nxe4] White just [m c3] played a quiet pawn move. What does it threaten? [h] The queen can [f d1a4 a4e8 a4e4] jump out with check, and hit your knight at the same time. [q 1 Threat?] [m c5 gaffe] Push your other pawn? The queen [m Qa4+] checks from the side. You block with a [m Nc6] knight. But look: now she simply [m Qxe4+ brillant] [z e4 1.3 2.0] [x impact] grabs your other knight. A fork! [p e4 e5 Nf3 Nf6 Nxe5 d6 Nf3 Nxe4 c3] Instead, push the [m d5 meilleur] center pawn: now the knight is [f d5e4] guarded, and the trick fails. Analyze your own game, free. Trap #6 tomorrow. Follow!""",
},
"finale_saavedra_1": {   # Saavedra : 1.c7 Rd6+ 2.Kb5 … 5.Kc2 Rd4 6.c8=R! (6.c8=Q Rc4+ 7.Qxc4 pat) 6…Ra4 7.Kb3 Rb4+ 8.Kxb4 (mat en 5, Stockfish) ; T14 B
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Don't make|a queen!",
    "voix": """White to play and win. The pawn runs forward. The rook checks from the side. The king walks up, and the checks keep coming, until the king hides next to his pawn. Now, make a queen? The rook checks right beside her. The queen must take, and Black has no move: stalemate! Follow: a new trick daily. So make a rook instead! The black rook must run, or it's mate in the corner. Now the king attacks it. Black gives one last check, and the king takes the rook. White wins!""",
    "script": """[p """ + SAAVEDRA + """] White to play and win. [h] [m c7] The pawn runs forward. The rook [m Rd6+] checks from the side. The king [m Kb5] walks up, and the checks keep coming, until the king [p """ + SAAVEDRA_CLE + """] hides next to his pawn. Now, [m c8=Q gaffe] make a queen? The rook [m Rc4+] checks right beside her. The queen must [m Qxc4] take, and Black has no move: [s tag a1 2.5 STALEMATE] [x impact] stalemate! Follow: a new trick daily. [p """ + SAAVEDRA_CLE + """] So make a [m c8=R brillant] [z c8 1.3 2.0] rook instead! The black rook must [m Ra4] run, or it's [f c8c1] mate in the corner. Now the king [m Kb3 brillant] attacks it. Black gives one last [m Rb4+] check, and the king takes the [m Kxb4] [x impact] rook. White wins!""",
},
})
QUESTIONS.update({
    "legende_miniature_1": "Follow: one new|trick a day",
    "legende_miniature_1_fr": "Abonne-toi :|un piège par jour",
    "touch_move_1": "Follow: one new|rule a day",
    "touch_move_1_fr": "Abonne-toi :|une règle par jour",
    "pigeon_en_19": "Trap #6 tomorrow|Follow!",
    "finale_saavedra_1": "Follow: a new|trick daily",
})

# 3/11 (exemple demandé par Simon, à itérer) : Smith-Morra, réserve n° 14 ; 6…a6?? 7.Cc7+ Dxc7 8.Fxc7 (+5,0), coup juste 6…e5 (−1,5) ; Stockfish 16 prof. 20
PERSO.update({
"exemple_morra_1": {
    "cote": "noirs", "sous_titres": "phrase",
    "hook": "One pawn move.|Queen gone.",
    "voix": """One natural pawn move, and Black loses the queen. Let's watch. White opens with the king's pawn, Black answers on the side. White gives a pawn right away. Black takes it. Then White offers a second pawn. Black grabs that one too. The knight takes back and jumps into the game. Black builds a solid wall. The bishop comes out. The black knight comes out. And now, the white knight jumps forward. It looks lonely, so Black kicks it with a pawn. Huge mistake! The knight jumps in with check, and it also attacks the rook. A royal fork! The queen has to take the knight. And the bishop takes the queen. White wins the queen for a knight! The problem was the hole next to the black king, guarded only by the queen. Better: push the center pawn and chase the bishop first. Watch the holes next to your king. Follow: one new trap every day.""",
    "script": """[p fen:rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR_w_KQkq_-_0_1] One natural pawn move, and Black loses the queen. [h] Let's watch. White opens with the [m e4] king's pawn, Black answers [m c5] on the side. White gives a [m d4] pawn right away. Black [m cxd4] takes it. Then White offers a [m c3] second pawn. Black grabs [m dxc3] that one too. The knight takes [m Nxc3] back and jumps into the game. Black builds a [m e6] solid wall. The bishop [m Bf4] comes out. The black knight [m Nc6] comes out. And now, the white knight [m Nb5 bizarre] jumps forward. It looks lonely, so Black kicks it [m a6 gaffe] with a pawn. Huge mistake! [q 1 Why?] The knight jumps [m Nc7+ brillant] [z c7 1.3 2.2] in with check, and it also attacks [f c7e8 c7a8] the rook. A royal fork! The queen has to [m Qxc7] take the knight. And the bishop [m Bxc7 brillant] [x impact] takes the queen. [s tag c7 3.0 QUEEN_WON] White wins the queen for a knight! [p e4 c5 d4 cxd4 c3 dxc3 Nxc3 e6 Bf4 Nc6 Nb5] The problem was the hole [f b5c7 b5d6] next to the black king, guarded only by the queen. Better: push the [m e5 meilleur] center pawn and chase [f e5f4] the bishop first. Watch the holes next to your king. Follow: one new trap every day.""",
},
})
QUESTIONS.update({"exemple_morra_1": "Follow: one new|trap every day"})

# 3/11 exemple v2 (Simon : « le plus important c'est le hook du début ») : démarre sur la tension, défi direct ; ouverture non rejouée (Studio : > 70 % partis en 3 s quand on la rejoue)
MORRA_CLE = "fen:r1bqkbnr/pp1p1ppp/2n1p3/1N6/4PB2/8/PP3PPP/R2QKBNR_b_KQkq_-_3_6"
PERSO.update({
"exemple_morra_2": {   # 3/11 v3 (Simon : « dans toutes les vidéos, avant de donner la réponse, on demande de s'abonner »)
    "cote": "noirs", "sous_titres": "phrase",
    "hook": "Kick this knight?|Your queen dies.",
    "voix": """Would you kick this knight? Most players do. Pawn up, the knight looks trapped. Is it safe? Follow for one new trap every day, and watch. It jumps in with check, and it hits the rook too. A royal fork! Your queen has to take it. And the bishop takes your queen. Queen gone, for one knight! The hole next to your king was guarded only by the queen. Better: push the center pawn and hit the bishop first. Would you have seen it?""",
    "script": """[p """ + MORRA_CLE + """] [f b5c7 b5d6] Would you kick this knight? [h] Most players do. Pawn [m a6 gaffe] [z a6 1.35 1.8] up, the knight looks trapped. Is it safe? [q 1 Safe?] Follow for one new trap every day, and watch. It jumps [m Nc7+ brillant] [z c7 1.5 2.4] in with check, and it hits [f c7e8 c7a8] the rook too. A royal fork! Your queen has to [m Qxc7] take it. And the bishop takes [m Bxc7 brillant] [z c7 1.5 2.6] [x impact] your queen. [s tag c7 3.0 QUEEN_GONE] Queen gone, for one knight! [p """ + MORRA_CLE + """] The hole [f b5c7] next to your king was guarded only by the queen. Better: push the [m e5 meilleur] center pawn and hit [f e5f4] the bishop first. Would you have seen it?""",
},
})
QUESTIONS.update({"exemple_morra_2": "Would you|have seen it?"})

# 4/11 (Producteur) : file du Scénariste du 3/11 ; coups vérifiés python-chess + Stockfish 16 (prof. 22) ; « Follow / Abonne-toi » juste avant la révélation (Simon, 3/11)
RETI = "fen:7K/8/k1P5/7p/8/8/8/8_w_-_-_0_1"
SCOTCH_PIEGE = "fen:r1bqk2r/pp2bppp/3p1n2/3Bp1B1/4P3/5N2/PPP2PPP/R2QK2R_w_KQkq_-_1_10"
EVERGREEN = "fen:1r2k1r1/pbppnp1p/1bn2P2/7q/Q7/B1PB1N2/P4PPP/3RR1K1_b_-_-_2_19"
PERSO.update({
"reti_etude_1": {   # Réti 1921 : 1.Kg7 h4 2.Kf6 Kb6 3.Ke5 Kxc6 4.Kf4 h3 5.Kg3 = (0,00 partout) ; 1.c7? / 1.Kh7? perdent (−34) ; 3…h3 4.Kd6 =
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "King too far.|Two pawns.",
    "voix": """White's king is far away. Black's pawn runs to queen, and your pawn is about to fall. Can White still draw? Follow for one new endgame trick every day, and watch. The king steps toward the runner. The pawn runs away. Another step, again diagonally. Black's king goes after your pawn. One more diagonal step! Now the king is near both pawns: if the pawn runs, yours queens too. So Black takes your pawn. But the king is back in the race. The pawn pushes again, and the king catches it. Draw! A diagonal king chases two targets at once.""",
    "script": """[p """ + RETI + """] White's king is far away. [h] Black's pawn [f h5h1] runs to queen, and your pawn [f a6c6] is about to fall. Can White still draw? [q 1 Draw?] Follow for one new endgame trick every day, and watch. The king [m Kg7 brillant] steps toward the runner. The pawn [m h4] runs away. Another step, [m Kf6] again diagonally. Black's king [m Kb6] goes after your pawn. One more [m Ke5 brillant] [z e5 1.3 2.0] diagonal step! Now the king is near [f e5d6 e5f4] both pawns: if the pawn runs, yours queens too. So Black [m Kxc6] takes your pawn. But the king is [m Kf4] back in the race. The pawn [m h3] pushes again, and the king [m Kg3] [x impact] catches it. [s tag g3 2.5 DRAW] Draw! A diagonal king chases two targets at once.""",
},
"reti_etude_1_fr": {   # jumeau FR de reti_etude_1 ; T13 B
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Roi trop loin.|Deux pions.",
    "voix": """Le roi blanc est très loin. Le pion noir file à dame, et ton pion va tomber. Les Blancs peuvent-ils encore faire nulle ? Abonne-toi : une astuce de finale par jour. Le roi avance vers le coureur. Le pion s'enfuit. Encore un pas, en diagonale. Le roi noir attaque ton pion. Encore une diagonale ! Le roi est près des deux pions : si le pion noir avance, le tien fait dame aussi. Alors les Noirs prennent ton pion. Mais le roi revient dans la course. Le pion avance encore, et le roi l'attrape. Nulle ! Un roi en diagonale vise deux cibles à la fois.""",
    "script": """[p """ + RETI + """] Le roi blanc est très loin. [h] Le pion noir [f h5h1] file à dame, et ton pion [f a6c6] va tomber. Les Blancs peuvent-ils encore faire nulle ? [q 1 Nulle ?] Abonne-toi : une astuce de finale par jour. Le roi [m Kg7 brillant] avance vers le coureur. Le pion [m h4] s'enfuit. Encore un pas, [m Kf6] en diagonale. Le roi noir [m Kb6] attaque ton pion. Encore une [m Ke5 brillant] [z e5 1.3 2.0] diagonale ! Le roi est près [f e5d6 e5f4] des deux pions : si le pion noir avance, le tien fait dame aussi. Alors les Noirs [m Kxc6] prennent ton pion. Mais le roi [m Kf4] revient dans la course. Le pion [m h3] avance encore, et le roi [m Kg3] [x impact] l'attrape. [s tag g3 2.5 NULLE] Nulle ! Un roi en diagonale vise deux cibles à la fois.""",
},
"decouverte_cavalier_1": {   # réserve n° 11 (Écossaise, 4 parties Lichess, ~1401) : 10.O-O?? (−4,1) Nxd5 11.Qxd5 Bxg5 12.Nxg5 Qxg5 ; coup juste 10.Bxf6 (+0,7) ; T11 B ; vers /try
    "cote": "noirs", "sous_titres": "phrase",
    "hook": "White castled.|Win a piece!",
    "voix": """White castles. Looks safe: every piece seems protected. But Black wins a piece by force. Can you find it? Follow for one new trap every day, and watch. The knight takes the bishop. The queen takes back. But look: that knight was hiding a bishop! Now bishop takes bishop. The white knight takes back, and then the black queen grabs the knight. Black is a whole piece up! White had to take the knight first. When a knight blocks a bishop, check what it hides. Analyze your own game, free.""",
    "script": """[p """ + SCOTCH_PIEGE + """] White [m O-O gaffe] castles. [h] Looks safe: every piece seems protected. But Black wins a piece by force. Can you find it? [q 1 Find_it?] Follow for one new trap every day, and watch. The knight [m Nxd5 brillant] takes the bishop. The queen [m Qxd5] takes back. But look: that knight was hiding [f e7g5] a bishop! Now bishop [m Bxg5] takes bishop. The white knight [m Nxg5] takes back, and then the black queen [m Qxg5 brillant] [z g5 1.3 2.0] [x impact] grabs the knight. [s tag g5 2.5 +1_PIECE] Black is a whole piece up! [p """ + SCOTCH_PIEGE + """] White had to take [m Bxf6 meilleur] the knight first. When a knight blocks [f e7g5] a bishop, check what it hides. Analyze your own game, free.""",
},
"decouverte_cavalier_1_fr": {   # jumeau FR de decouverte_cavalier_1
    "cote": "noirs", "sous_titres": "phrase",
    "hook": "Les Blancs roquent.|Gagne une pièce !",
    "voix": """Les Blancs roquent. Tout a l'air protégé. Mais les Noirs gagnent une pièce de force. Tu la vois ? Abonne-toi : un piège par jour pour monter ton Elo. Le cavalier prend le fou. La dame reprend. Mais regarde : ce cavalier cachait un fou ! Fou prend fou. Le cavalier blanc reprend, et la dame noire croque le cavalier. Les Noirs ont une pièce de plus ! Il fallait d'abord prendre le cavalier. Quand un cavalier bloque ton fou, regarde ce qu'il cache.""",
    "script": """[p """ + SCOTCH_PIEGE + """] Les Blancs [m O-O gaffe] roquent. [h] Tout a l'air protégé. Mais les Noirs gagnent une pièce de force. Tu la vois ? [q 1 Trouve-la !] Abonne-toi : un piège par jour pour monter ton Elo. Le cavalier [m Nxd5 brillant] prend le fou. La dame [m Qxd5] reprend. Mais regarde : ce cavalier cachait [f e7g5] un fou ! Fou [m Bxg5] prend fou. Le cavalier blanc [m Nxg5] reprend, et la dame noire [m Qxg5 brillant] [z g5 1.3 2.0] [x impact] croque le cavalier. [s tag g5 2.5 +1_PIÈCE] Les Noirs ont une pièce de plus ! [p """ + SCOTCH_PIEGE + """] Il fallait d'abord [m Bxf6 meilleur] prendre le cavalier. Quand un cavalier bloque [f e7g5] ton fou, regarde ce qu'il cache.""",
},
"evergreen_1": {   # Anderssen–Dufresne, Berlin 1852 (partie complète rejouée, légale) : 19…Qxf3? (19…Bd4! tient) 20.Rxe7+ Nxe7 21.Qxd7+ Kxd7 22.Bf5+ (échec double) Ke8 23.Bd7+ Kf8 24.Bxe7# ; menace 20…Qxg2# vérifiée
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "A free knight?|Not quite!",
    "voix": """Black's queen grabs a knight, and threatens mate next move. White is lost? No! Adolf Anderssen, Berlin, 1852, finds a killer idea. Can you see it? Follow for one new trap every day, and watch. Rook takes the knight, check! The knight takes back. Now the queen takes, check! The king has to take her. And now, double check! The king steps back. The same bishop checks again. The king takes one more step. And now the bishop, protected by its partner, takes: checkmate! They call it the Evergreen Game. Would you have sacrificed the queen?""",
    "script": """[p """ + EVERGREEN + """] Black's queen [m Qxf3 gaffe] grabs a knight, [h] and threatens [f f3g2] mate next move. White is lost? No! Adolf Anderssen, Berlin, 1852, finds a killer idea. Can you see it? [q 1 Find_it?] Follow for one new trap every day, and watch. Rook [m Rxe7+ brillant] takes the knight, check! The knight [m Nxe7] takes back. Now the queen [m Qxd7+ brillant] [z d7 1.3 2.0] takes, check! The king has [m Kxd7] to take her. And now, [m Bf5+ brillant] [f f5d7 d1d7] double check! The king [m Ke8] steps back. The same bishop [m Bd7+] checks again. The king takes one more [m Kf8] step. And now the bishop, protected [f a3e7] by its partner, [m Bxe7# mat] [x impact] takes: checkmate! They call it the Evergreen Game. Would you have sacrificed the queen?""",
},
})
QUESTIONS.update({
    "reti_etude_1": "Would you have|found it?",
    "reti_etude_1_fr": "Tu l'aurais|trouvé ?",
    "decouverte_cavalier_1": "Analyze your own|game, free",
    "decouverte_cavalier_1_fr": "Tu l'aurais|vu ?",
    "evergreen_1": "Would you sacrifice|the queen?",
})

# 5/11 (Producteur) : file du Scénariste du 4/11 ; lignes vérifiées python-chess + Stockfish 16 ; « Follow / Abonne-toi » juste avant la révélation (Simon, 3/11)
PERSO.update({
"dame_pion_1": {   # 1.Qd5+ Kb1 2.Qb3+ Ka1 3.Kf6 c1=Q = (0,00 à chaque coup) ; 3.Qxc2 pat (python-chess) ; tous les coups blancs après 2…Ka1 = 0,00
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Queen vs pawn.|Can White win?",
    "voix": """White has a queen. Black has only a pawn, but it queens next move. Can White win? Follow: one new endgame trick every day. Check! The king runs. Check again! It hides in the corner. Now, take the pawn? Stalemate! Black has no legal move. So White brings the king closer instead. But now the pawn queens. Queen against queen: a draw! With a bishop's pawn, the corner saves Black when the enemy king is far.""",
    "script": """[p fen:8/8/6K1/4Q3/8/8/k1p5/8_w_-_-_0_1] [f c2c1] White has a queen. [h] Black has only a pawn, but it queens next move. Can White win? [q 1 Win?] Follow: one new endgame trick every [m Qd5+] day. Check! [m Kb1] The king runs. Check [m Qb3+] again! It hides in the [m Ka1] corner. Now, take the [m Qxc2 gaffe] [z a1 1.3 2.0] pawn? [s tag a1 2.5 STALEMATE] Stalemate! Black has no legal move. [p fen:8/8/6K1/8/8/1Q6/2p5/k7_w_-_-_4_3] So White brings [m Kf6] the king closer instead. But now the pawn [m c1=Q] [x impact] queens. Queen against queen: [s tag c1 2.5 DRAW] a draw! With a bishop's pawn, the corner saves Black when the enemy king is far.""",
},
"dame_pion_1_fr": {   # jumeau FR de dame_pion_1 ; T13 B
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Dame contre pion.|Gagné ?",
    "voix": """Les Blancs ont une dame. Les Noirs n'ont qu'un pion, mais il va faire dame. Les Blancs peuvent-ils gagner ? Abonne-toi : une astuce de finale par jour. Échec ! Le roi fuit. Encore échec ! Il se cache dans le coin. Alors, on prend le pion ? Pat ! Les Noirs n'ont plus aucun coup. Les Blancs rapprochent donc leur roi. Mais le pion fait dame. Dame contre dame : nulle ! Avec un pion de fou, le coin sauve les Noirs quand le roi adverse est loin.""",
    "script": """[p fen:8/8/6K1/4Q3/8/8/k1p5/8_w_-_-_0_1] [f c2c1] Les Blancs ont une dame. [h] Les Noirs n'ont qu'un pion, mais il va faire dame. Les Blancs peuvent-ils gagner ? [q 1 Gagné ?] Abonne-toi : une astuce de finale par [m Qd5+] jour. Échec ! [m Kb1] Le roi fuit. Encore [m Qb3+] échec ! Il se cache [m Ka1] dans le coin. Alors, on prend [m Qxc2 gaffe] [z a1 1.3 2.0] le pion ? [s tag a1 2.5 PAT] Pat ! Les Noirs n'ont plus aucun coup. [p fen:8/8/6K1/8/8/1Q6/2p5/k7_w_-_-_4_3] Les Blancs rapprochent [m Kf6] donc leur roi. Mais le pion [m c1=Q] [x impact] fait dame. Dame contre dame : [s tag c1 2.5 NULLE] nulle ! Avec un pion de fou, le coin sauve les Noirs quand le roi adverse est loin.""",
},
"nimzo_intermezzo_1": {   # réserve n° 17 (Nimzo-Léningrad, 3 parties Lichess) : 7.Fxf6? (−6,0 ; 7.Fd2 +0,35) Bxc3+ 8.bxc3 Qxc3+ 9.Qd2 Qxa1+ 10.Qd1 Qxd1+ 11.Kxd1 gxf6 (−6,0) ; 7…gxf6 = 0,00
    "cote": "noirs", "sous_titres": "phrase",
    "hook": "Don't recapture.|Check first!",
    "voix": """White just took your knight. Take back, and it's equal. But look at that white knight: pinned to the king, and attacked twice. Can you win more? Follow: one new trap every day. The bishop takes, check! The pawn takes back. The queen takes, check, and she hits the rook too. White blocks with the queen. The queen grabs the rook, check! White blocks again. You trade the queens, and the king takes back. Only now, you take back the bishop. A full rook up! Check first, recapture later.""",
    "script": """[p fen:rnb1k2r/pp1p1ppp/4pB2/q7/1bPN4/2N5/PP2PPPP/R2QKB1R_b_KQkq_-_0_7] [f b4e1 a5c3] White just took your knight. [h] Take back, and it's equal. But look at that white knight: pinned to the king, and attacked twice. Can you win more? [q 1 Find_it!] Follow: one new trap every day. The bishop [m Bxc3+ brillant] takes, check! The pawn [m bxc3] takes back. The queen [m Qxc3+ brillant] [z c3 1.3 2.0] takes, check, and she hits [f c3a1 c3e1] the rook too. White blocks [m Qd2] with the queen. The queen [m Qxa1+] [x impact] grabs the rook, check! White [m Qd1] blocks again. You [m Qxd1+] trade the queens, and the king [m Kxd1] takes back. Only now, you take [m gxf6] back the bishop. [s tag f6 2.5 +1_ROOK] A full rook up! Check first, recapture later.""",
},
"nimzo_intermezzo_1_fr": {   # jumeau FR de nimzo_intermezzo_1
    "cote": "noirs", "sous_titres": "phrase",
    "hook": "Ne reprends pas.|Échec d'abord !",
    "voix": """Les Blancs viennent de prendre ton cavalier. Si tu reprends, c'est égal. Mais regarde ce cavalier blanc : cloué sur son roi, et attaqué deux fois. Tu trouves mieux ? Abonne-toi : un piège par jour pour monter ton Elo. Le fou prend, échec ! Le pion reprend. La dame prend, échec, et elle vise aussi la tour. Les Blancs bloquent avec la dame. La dame croque la tour, échec ! Les Blancs bloquent encore. Tu échanges les dames, et le roi reprend. Et seulement maintenant, tu reprends le fou. Une tour de plus ! Échec d'abord, reprise ensuite.""",
    "script": """[p fen:rnb1k2r/pp1p1ppp/4pB2/q7/1bPN4/2N5/PP2PPPP/R2QKB1R_b_KQkq_-_0_7] [f b4e1 a5c3] Les Blancs viennent de prendre ton cavalier. [h] Si tu reprends, c'est égal. Mais regarde ce cavalier blanc : cloué sur son roi, et attaqué deux fois. Tu trouves mieux ? [q 1 Trouve-le !] Abonne-toi : un piège par jour pour monter ton Elo. Le fou [m Bxc3+ brillant] prend, échec ! Le pion [m bxc3] reprend. La dame [m Qxc3+ brillant] [z c3 1.3 2.0] prend, échec, et elle vise [f c3a1 c3e1] aussi la tour. Les Blancs bloquent [m Qd2] avec la dame. La dame [m Qxa1+] [x impact] croque la tour, échec ! Les Blancs [m Qd1] bloquent encore. Tu [m Qxd1+] échanges les dames, et le roi [m Kxd1] reprend. Et seulement maintenant, tu reprends [m gxf6] le fou. [s tag f6 2.5 +1_TOUR] Une tour de plus ! Échec d'abord, reprise ensuite.""",
},
"petrov_cavalier_mat3_1": {   # réserve n° 16 (Petrov, 3 parties Lichess, ~1841) : 7…Ng3+ 8.hxg3 (Kg1 illégal : Fc5) Qh6+ 9.Qh5 Qxh5# (#−3 vérifié) ; vers /try
    "cote": "noirs", "sous_titres": "phrase",
    "hook": "King in the corner.|Mate in 3!",
    "voix": """White just hid his king in the corner. It looks safe. But Black has mate in three. Can you find it? Follow: one new trap every day. The knight jumps in, check! The pawn must take: the bishop guards the other square. The queen slides over, check! White can only block with the queen. The queen takes: checkmate! The far bishop shuts the last door. Analyze your own game, free.""",
    "script": """[p fen:rnb1k2r/ppp2ppp/5q2/2bpN3/4nP2/3B4/PPPP2PP/RNBQ1R1K_b_kq_-_2_7] [s tag h1 2.0 SAFE?] White just hid his king in the corner. [h] It looks safe. But Black has mate in three. Can you find it? [q 1 Find_it?] Follow: one new trap every day. The knight [m Ng3+ brillant] [z g3 1.3 2.0] jumps in, check! The pawn [m hxg3] must take: the bishop [f c5g1] guards the other square. The queen [m Qh6+ brillant] slides over, check! White can only [m Qh5] block with the queen. The queen [m Qxh5# mat] [z h5 1.3 2.0] [x impact] takes: checkmate! The far bishop [f c5g1] shuts the last door. Analyze your own game, free.""",
},
"echange_pions_1": {   # position composée : 1.Rxc7+ Kxc7 2.gxh6 Kd8 3.h7 Ke7 4.h8=Q (#+14 après 1.Rxc7+) ; 1.Rxe6 / 1.Rd6 ≈ 0,00
    "cote": "blancs", "sous_titres": "phrase",
    "hook": "Rook attacked twice.|Don't run!",
    "voix": """Your rook is attacked twice. Grab a pawn? Run away? There is a much stronger idea. Can you find it? Follow: one new idea every day. Trade the rooks, check! The king takes back. Now the pawn takes, and look: the black king is far away. The king runs. The white pawn steps up. The king runs again. Too late: the pawn becomes a queen! Before you trade, count the distance.""",
    "script": """[p fen:8/1kr5/2R1pp1p/6P1/4PP2/8/4K3/8_w_-_-_0_1] [f b7c6 c7c6] Your rook is attacked twice. [h] Grab a pawn? Run away? There is a much stronger idea. Can you find it? [q 1 Find_it?] Follow: one new idea every day. Trade [m Rxc7+ brillant] the rooks, check! The king [m Kxc7] takes back. Now the pawn [m gxh6 brillant] [z h6 1.3 2.0] takes, and look: the black king [f h6h8] is far away. [m Kd8] The king runs. The white pawn [m h7] steps up. The king [m Ke7] runs again. Too late: the pawn [m h8=Q] [x impact] becomes a queen! [s tag h8 2.5 QUEEN] Before you trade, count the distance.""",
},
})
QUESTIONS.update({
    "dame_pion_1": "Would you have|taken the pawn?",
    "dame_pion_1_fr": "Tu aurais pris|le pion ?",
    "nimzo_intermezzo_1": "Would you have|recaptured?",
    "nimzo_intermezzo_1_fr": "Tu aurais|repris ?",
    "petrov_cavalier_mat3_1": "Analyze your own|game, free",
    "echange_pions_1": "Would you have|grabbed the pawn?",
})

# 6/11 (Producteur) : file du Scénariste du 5/11 ; lignes vérifiées python-chess + Stockfish 16 ; « Follow / Abonne-toi » juste avant la révélation (Simon, 3/11)
# E3 de la file (Dragon « dame sans case ») = DÉJÀ FAIT en EN (pigeon_en_17, 1/11) → remplacé par la réserve n° 4 (Scandinave, Qa4?? Nd6+! dégagement puis Bb5+)
import re as _re
def _lu(script):   # texte lu EN = script sans repères (cases dites telles quelles)
    return _re.sub(r"\s+", " ", _re.sub(r"\[[^\]]*\]", "", script)).strip()
DEEPBLUE = "fen:r1bqkb1r/pp1n1ppp/2p1pn2/6N1/3P4/3B1N2/PPP2PPP/R1BQK2R_b_KQkq_-_1_7"
LUCENA = "fen:1K1k4/1P6/8/8/8/8/r7/2R5_w_-_-_0_1"
SCANDI = "fen:r1b1kbnr/ppp1pppp/n7/qN5Q/8/B7/P1PP1PPP/R3KBNR_b_KQkq_-_5_7"
MARSHALL = "fen:r1bqk2r/1p2nppp/p1n1p3/2bpP3/8/2NB1N2/PPP2PPP/R1BQ1RK1_b_kq_-_3_8"
_S = {
"deepblue_g6_1": ("blancs", "Kasparov. Move seven.|h6?",   # Deep Blue – Kasparov, New York, 11/5/1997, partie 6 : 7…h6 8.Nxe6 … 19.c4 1-0 ; Stockfish +1,1 → +4,6 (jamais « mat »)
"""[p """ + DEEPBLUE + """] May 1997: Kasparov against the computer Deep Blue. He plays [m h6 gaffe] h6. [h] See the punishment? [q 1 Find_it?] Follow: one new chess story every day. The knight [m Nxe6 brillant] [z e6 1.3 2.0] takes! The queen [m Qe7] steps aside. White [m O-O] castles, and Black [m fxe6] takes the knight. But his king can't castle now. Bishop [m Bg6+ brillant] check! The king [m Kd8] runs. A bishop [m Bf4] comes out. Black [m b5] pushes, White [m a4] hits back. The bishop [m Bb7] develops. The rook [m Re1] joins. A knight [m Nd5] jumps in. The bishop [m Bg3] steps back. The king [m Kc8] runs again. White [m axb5] opens a file, Black [m cxb5] takes back. The queen [m Qd3] comes in. The bishop [m Bc6] guards. Now, [m Bf5 brillant] [z f5 1.3 2.0] bishop to f5! Black [m exf5] takes, the file opens, and the rook [m Rxe7] [x impact] takes the queen! The bishop [m Bxe7] takes back, the pawn [m c4] pushes, [s tag c8 2.5 1-0] and Kasparov resigned."""),
"finale_lucena_1": ("blancs", "Rook endgame.|Can White win?",   # Lucena : 1.Rd1+ Ke7 2.Rd4 Ra1 3.Kc7 Rc1+ 4.Kb6 Rb1+ 5.Kc6 Rc1+ 6.Kb5 Rb1+ 7.Rb4 Rxb4+ 8.Kxb4 Kd7 9.b8=Q (Stockfish +5 → mat ; une manière de gagner)
"""[p """ + LUCENA + """] [f a2a8] White's pawn is one step from queening, but its own king is in the way. [h] Can White win? [q 1 Win?] Follow: one new endgame trick every day. Rook [m Rd1+ brillant] check, the king [m Ke7] is pushed away. Now the key: the rook [m Rd4 brillant] [z d4 1.3 2.0] goes to the fourth rank. The bridge! Black [m Ra1] waits. The king [m Kc7] walks out. Check [m Rc1+] from behind, the king [m Kb6] steps down. Check [m Rb1+] again, the king [m Kc6] comes up. Check [m Rc1+] once more, the king [m Kb5] goes on. One more [m Rb1+] check, and the rook [m Rb4 brillant] [z b4 1.3 2.0] blocks! The rooks [m Rxb4+] are traded, the king [m Kxb4] takes back. Too late [m Kd7] for Black: the pawn [m b8=Q] [x impact] queens! [s tag b8 2.5 BRIDGE] Build the bridge."""),
"scandi_degagement_1": ("blancs", "King and queen|on one line...",   # réserve n° 4 (Scandinave, 3 parties Lichess, ~1646) : 7…Qa4?? (7…Qb6 −0,5) 8.Nd6+! exd6 9.Bb5+ Qxb5 10.Qxb5+ (+3,7 ; 9…Bd7 10.Bxa4 +3,8) ; vers /try
"""[p """ + SCANDI + """] Black's queen [m Qa4 gaffe] comes to attack your bishop. [h] But look: king and queen [f e8a4] on one diagonal, and only your knight is in the way. Can you see White's move? [q 1 Find_it?] Follow: one new trap every day. Knight [m Nd6+ brillant] [z d6 1.3 2.0] check! It clears the square, and Black [m exd6] takes. Now bishop [m Bb5+ brillant] check, hitting [f b5e8 b5a4] the king and the queen! The queen [m Qxb5] takes, and your queen [m Qxb5+] [x impact] takes back. [s tag b5 2.5 +QUEEN] A queen for a knight and a bishop! Analyze your own game, free."""),
"marshall_grec_1": ("blancs", "Castle?|Greek gift!",   # réserve n° 10 (Sicilienne gambit Marshall, 4 parties Lichess, ~1490) : 8…O-O? (8…Bd7 −0,15) 9.Bxh7+ … 17.Qxg7 (+4,2 → +5,5) ; 11…Re8 empêche le mat : on ne dit pas « mat imparable »
"""[p """ + MARSHALL + """] Black [m O-O gaffe] castles. Looks safe? [h] No knight on f6 guards h7. Find the famous idea! [q 1 Find_it?] Follow: one new trap every day. Bishop [m Bxh7+ brillant] [z h7 1.3 2.0] takes h7, check! The king [m Kxh7] takes it. The knight [m Ng5+ brillant] checks! The king [m Kg8] steps back. The queen [m Qh5] comes, threatening mate. The rook [m Re8] makes room. Queen [m Qh7+] check! The king [m Kf8] runs away. Check [m Qh8+] again! A knight [m Ng8] blocks. The other knight [m Nh7+] checks! The king [m Ke7] steps out. Now the bishop [m Bg5+ brillant] [z d8 1.3 2.0] checks, with the queen behind! The king [m Kd7] hides, the bishop [m Bxd8] [x impact] takes the queen, and the rook [m Rxd8] takes back. [s tag d8 2.5 +QUEEN] Pawn on e5, knight to g5: the sacrifice works."""),
"finale_lucena_1_fr": ("blancs", "Finale de tours.|Gagné ?",   # jumeau FR de finale_lucena_1 ; T13 B
"""[p """ + LUCENA + """] [f a2a8] Le pion blanc va faire dame, mais son propre roi bloque la route. [h] Les Blancs gagnent ? [q 1 Gagné ?] Abonne-toi : une astuce de finale par jour. La tour [m Rd1+ brillant] donne échec, le roi [m Ke7] est repoussé. Le coup clé : la tour [m Rd4 brillant] [z d4 1.3 2.0] va sur la quatrième rangée. C'est le pont ! Les Noirs [m Ra1] attendent. Le roi [m Kc7] sort. Échec [m Rc1+] par derrière, le roi [m Kb6] descend. Encore [m Rb1+] échec, le roi [m Kc6] remonte. Échec [m Rc1+] de nouveau, le roi [m Kb5] continue. Un dernier [m Rb1+] échec, et la tour [m Rb4 brillant] [z b4 1.3 2.0] s'interpose ! Les tours [m Rxb4+] s'échangent, le roi [m Kxb4] reprend. Trop tard [m Kd7] pour les Noirs : le pion [m b8=Q] [x impact] fait dame ! [s tag b8 2.5 LE_PONT] Construis le pont."""),
"scandi_degagement_1_fr": ("blancs", "Roi et dame|sur une ligne...",   # jumeau FR de scandi_degagement_1
"""[p """ + SCANDI + """] La dame noire [m Qa4 gaffe] vient attaquer ton fou. [h] Mais regarde : le roi et la dame [f e8a4] sont sur la même diagonale, et seul ton cavalier gêne. Tu vois le coup des Blancs ? [q 1 Trouve-le !] Abonne-toi : un piège par jour. Cavalier, [m Nd6+ brillant] [z d6 1.3 2.0] échec ! Il libère la case, et les Noirs [m exd6] le prennent. Puis le fou [m Bb5+ brillant] donne échec, et vise [f b5e8 b5a4] aussi la dame ! La dame [m Qxb5] prend, et ta dame [m Qxb5+] [x impact] reprend. [s tag b5 2.5 +DAME] Une dame pour un cavalier et un fou ! Roi et dame sur une ligne ? Cherche l'échec."""),
}
PERSO.update({k: {"cote": c, "sous_titres": "phrase", "hook": h, "script": sc, "voix": _lu(sc)} for k, (c, h, sc) in _S.items()})
QUESTIONS.update({
    "deepblue_g6_1": "Would you take|the knight?",
    "finale_lucena_1": "Could you build|the bridge?",
    "scandi_degagement_1": "Analyze your own|game, free",
    "marshall_grec_1": "Would you sacrifice|the bishop?",
    "finale_lucena_1_fr": "Tu aurais construit|le pont ?",
    "scandi_degagement_1_fr": "Tu l'aurais|vu ?",
})

# 6/11 (Producteur) : coups recalés d'après sorties/minutage/ (écart minimal relevé), même texte lu = voix réutilisée (0 crédit)
PERSO_RECAL = {
    'deepblue_g6_1': "[p fen:r1bqkb1r/pp1n1ppp/2p1pn2/6N1/3P4/3B1N2/PPP2PPP/R1BQK2R_b_KQkq_-_1_7] May 1997: Kasparov against the computer Deep Blue. He plays [m h6 gaffe] h6. [h] See the punishment? [q 1 Find_it?] Follow: one new chess story every day. The knight [m Nxe6 brillant] [z e6 1.3 2.0] takes! The queen [m Qe7] steps aside. [m O-O] White castles, and Black [m fxe6] takes the knight. But his king can't castle now. Bishop [m Bg6+ brillant] check! The king [m Kd8] runs. A bishop [m Bf4] comes out. [m b5] Black pushes, White [m a4] hits back. The bishop [m Bb7] develops. The rook [m Re1] joins. A knight [m Nd5] jumps in. The bishop [m Bg3] steps back. The king [m Kc8] runs again. White [m axb5] opens a file, Black [m cxb5] takes back. The queen [m Qd3] comes in. The bishop [m Bc6] guards. Now, [m Bf5 brillant] [z f5 1.3 2.0] bishop to f5! Black [m exf5] takes, the file opens, and the rook [m Rxe7] [x impact] takes the queen! The bishop [m Bxe7] takes back, the pawn [m c4] pushes, [s tag c8 2.5 1-0] and Kasparov resigned.",   # écart min estimé 1.34 s
    'finale_lucena_1': "[p fen:1K1k4/1P6/8/8/8/8/r7/2R5_w_-_-_0_1] [f a2a8] White's pawn is one step from queening, but its own king is in the way. [h] Can White win? [q 1 Win?] Follow: one new endgame trick every day. [m Rd1+ brillant] Rook check, the king [m Ke7] is pushed away. Now the key: the rook [m Rd4 brillant] [z d4 1.3 2.0] goes to the fourth rank. The bridge! Black [m Ra1] waits. The king [m Kc7] walks out. Check [m Rc1+] from behind, the king [m Kb6] steps down. [m Rb1+] Check again, the king [m Kc6] comes up. Check [m Rc1+] once more, the king [m Kb5] goes on. One [m Rb1+] more check, and the rook [m Rb4 brillant] [z b4 1.3 2.0] blocks! The [m Rxb4+] rooks are traded, the king [m Kxb4] takes back. Too late [m Kd7] for Black: the pawn [m b8=Q] [x impact] queens! [s tag b8 2.5 BRIDGE] Build the bridge.",   # écart min estimé 1.30 s
    'scandi_degagement_1': "[p fen:r1b1kbnr/ppp1pppp/n7/qN5Q/8/B7/P1PP1PPP/R3KBNR_b_KQkq_-_5_7] Black's queen [m Qa4 gaffe] comes to attack your bishop. [h] But look: king and queen [f e8a4] on one diagonal, and only your knight is in the way. Can you see White's move? [q 1 Find_it?] Follow: one new trap every day. [m Nd6+ brillant] [z d6 1.3 2.0] Knight check! It clears the square, and [m exd6] Black takes. Now bishop check, [m Bb5+ brillant] hitting [f b5e8 b5a4] the king and the queen! The queen [m Qxb5] takes, and your queen takes back. [s tag b5 2.5 +QUEEN] [m Qxb5+] [x impact] A queen for a knight and a bishop! Analyze your own game, free.",   # écart min estimé 2.55 s
    'marshall_grec_1': '[p fen:r1bqk2r/1p2nppp/p1n1p3/2bpP3/8/2NB1N2/PPP2PPP/R1BQ1RK1_b_kq_-_3_8] Black [m O-O gaffe] castles. Looks safe? [h] No knight on f6 guards h7. Find the famous idea! [q 1 Find_it?] Follow: one new trap every day. Bishop [m Bxh7+ brillant] [z h7 1.3 2.0] takes h7, check! The king [m Kxh7] takes it. The knight [m Ng5+ brillant] checks! The king [m Kg8] steps back. The queen [m Qh5] comes, threatening mate. The rook [m Re8] makes room. Queen [m Qh7+] check! The king [m Kf8] runs away. Check [m Qh8+] again! A knight [m Ng8] blocks. The other knight [m Nh7+] checks! The king [m Ke7] steps out. Now the bishop [m Bg5+ brillant] [z d8 1.3 2.0] checks, with the queen behind! [m Kd7] The king hides, the bishop [m Bxd8] [x impact] takes the queen, and the rook [m Rxd8] takes back. [s tag d8 2.5 +QUEEN] Pawn on e5, knight to g5: the sacrifice works.',   # écart min estimé 1.48 s
    'scandi_degagement_1_fr': "[p fen:r1b1kbnr/ppp1pppp/n7/qN5Q/8/B7/P1PP1PPP/R3KBNR_b_KQkq_-_5_7] La dame noire [m Qa4 gaffe] vient attaquer ton fou. [h] Mais regarde : le roi et la dame [f e8a4] sont sur la même diagonale, et seul ton cavalier gêne. Tu vois le coup des Blancs ? [q 1 Trouve-le !] Abonne-toi : un piège par jour. Cavalier, [m Nd6+ brillant] [z d6 1.3 2.0] échec ! Il libère la case, et les [m exd6] Noirs le prennent. Puis le fou donne [m Bb5+ brillant] échec, et vise [f b5e8 b5a4] aussi la dame ! [m Qxb5] La dame prend, et ta dame reprend. [s tag b5 2.5 +DAME] [m Qxb5+] [x impact] Une dame pour un cavalier et un fou ! Roi et dame sur une ligne ? Cherche l'échec.",   # écart min estimé 2.98 s
}
for _k, _sc in PERSO_RECAL.items(): PERSO[_k]['script'] = _sc

# 7/11 (Producteur) : file du Scénariste du 6/11 ; lignes vérifiées python-chess + Stockfish 16 (prof. 20) ; « Follow / Abonne-toi » juste avant la révélation (Simon, 3/11)
PERCEE = "fen:7k/ppp5/8/PPP5/8/8/8/K7_w_-_-_0_1"
LASKER = "fen:r4rk1/1b2bppp/ppq1pn2/2ppB2N/5P2/1P1BP3/P1PPQ1PP/R4RK1_b_-_-_1_14"
STANLEY = "fen:r1b1k1nr/pppp1pQ1/8/2bNp2p/2BnP2q/7N/PPPP2PP/R1BK3R_w_kq_-_3_9"
MAUVAIS_FOU = "fen:7k/8/5K2/7P/8/3B4/8/8_w_-_-_0_1"
_S = {
"percee_3v3_1": ("blancs", "Three pawns each.|One push wins.",   # 1.b6! axb6 2.c6! bxc6 3.a6 b5 4.a7 b4 5.a8=Q ; Stockfish : 1.b6 +5,6/+7 ; 1.a6 −6,9 ; 1.c6 −6,3
"""[p """ + PERCEE + """] [f b5b6 a5a6 c5c6] Three pawns against three, and both kings are far away. [h] White to move: one push wins, the others lose. Can you find it? [q 1 Which_one?] Follow: one new endgame trick every day. Pawn to [m b6 brillant] [z b6 1.3 2.0] b6! If Black takes with the [m axb6] a-pawn, then the c-pawn jumps [m c6 brillant] to c6! Black has to [m bxc6] take again, but now nothing can stop the a-pawn. It runs [m a6] to a6. Black's pawn [m b5] runs too, one step slow. The [m a7] pawn reaches a7. One more [m b4] step for Black, and the a-pawn [m a8=Q] [x impact] [z a8 1.3 2.0] queens! [s tag a8 2.5 QUEEN] Give two pawns to free one."""),
"lasker_bauer_1": ("blancs", "Lasker, 1889.|Two bishops. Gone.",   # Lasker – Bauer, Amsterdam 1889 (Wikipédia) : 14…Nxh5 15.Bxh7+ … 23.Qxb7 (1–0 au 38e) ; Stockfish +1,7 → +4,5 → +5,1 ; jamais « mat » ni « coup fatal »
"""[p """ + LASKER + """] [f h5f6] Amsterdam, 1889. Lasker offers a knight on h5, [h] and Black [m Nxh5 gaffe] takes it. Can you see White's reply? [q 1 Find_it?] Follow: one new chess story every day. Bishop [m Bxh7+ brillant] [z h7 1.3 2.0] takes h7, check! The king [m Kxh7] takes it. The queen takes [m Qxh5+] the knight, check. The king [m Kg8] steps back, and the second bishop [m Bxg7 brillant] [z g7 1.3 2.0] takes g7! The king [m Kxg7] takes again, and the queen gives [m Qg4+] check. The king hides [m Kh7] in the corner. Now the rook [m Rf3] swings to f3. Black [m e5] pushes a pawn, and the rook [m Rh3+] slides to h3, check! Black blocks [m Qh6] with the queen, and the rook [m Rxh6+] [x impact] takes her with check. The king [m Kxh6] takes back. Then the queen [m Qd7] [f d7b7 d7e7] forks two bishops. Black [m Bf6] saves one, and the queen takes [m Qxb7] the other. [s tag b7 2.5 1-0] Lasker wins."""),
"vienne_stanley_1": ("blancs", "Free rook.|Take it?",   # réserve n° 19 (Vienne, Stanley, 2 parties Lichess ~1740) : 9.Qxh8?? (9.c3 +4,2) Qg4+ 10.Ke1 Nxc2+ 11.Kf1 Qd1# ; après Qg4+ deux réponses (Ke1, Be2), les deux perdent
"""[p """ + STANLEY + """] [f g7h8] White to move. A rook on h8 has no defender. [h] Should he take it? [q 1 Take_it?] Follow: one new trap every day. He [m Qxh8 gaffe] takes. Queen check [m Qg4+ brillant] [z g4 1.3 2.0] on g4! White has two replies, and both lose. The king [m Ke1] goes to e1. Now the knight [m Nxc2+ brillant] [f c2e1 c2a1] takes c2, check, and forks the rook. The king [m Kf1] runs to f1, and the queen [m Qd1# mat] [x impact] [z d1 1.3 2.0] goes to d1. Checkmate! [s tag d1 2.5 MATE] Analyze your own game, free."""),
"fou_mauvaise_couleur_1": ("blancs", "Bishop and pawn up.|Can White win?",   # fou de mauvaise couleur + pion de tour (théorie classique, « Wrong rook pawn ») : 1.h6 Kg8 2.Bf5 Kh8 3.Bg6 Kg8 4.h7+ Kh8 5.Kf7 pat ; Stockfish ≈ 0,0 partout
"""[p """ + MAUVAIS_FOU + """] White has an extra bishop and a pawn. Black has only a king. [h] Can White win? [q 1 Win?] Follow: one new endgame trick every day. No! The pawn [m h6] marches up. The black king [m Kg8] steps out of the corner. The bishop [m Bf5] comes closer, and the king [m Kh8] goes back. The bishop [m Bg6] tries again, so the king [m Kg8] steps out again. [m h7+] Pawn to h7, check! The king [m Kh8] hides in the corner. And now the white king steps [m Kf7] [z h8 1.3 2.0] closer: stalemate! [s tag h8 2.5 DRAW] The bishop can never control that dark corner square. Check your bishop's colour before you trade."""),
"lasker_bauer_1_fr": ("blancs", "Lasker, 1889.|Deux fous donnés.",   # jumeau FR de lasker_bauer_1
"""[p """ + LASKER + """] [f h5f6] Amsterdam, 1889. Lasker offre un cavalier en h5, [h] et les Noirs [m Nxh5 gaffe] le prennent. Tu vois la réponse des Blancs ? [q 1 Trouve-la !] Abonne-toi : une histoire d'échecs par jour. Le fou [m Bxh7+ brillant] [z h7 1.3 2.0] prend h7, échec ! Le roi [m Kxh7] le prend. La dame prend [m Qxh5+] le cavalier, échec. Le roi [m Kg8] recule, et le deuxième fou [m Bxg7 brillant] [z g7 1.3 2.0] prend g7 ! Le roi [m Kxg7] prend encore, et la dame donne [m Qg4+] échec. Le roi se [m Kh7] cache. Puis la tour [m Rf3] passe en f3. Les Noirs [m e5] poussent un pion, et la tour glisse [m Rh3+] en h3, échec ! Les Noirs bloquent [m Qh6] avec la dame, et la tour la [m Rxh6+] [x impact] prend, avec échec. Le roi [m Kxh6] reprend. Enfin la dame [m Qd7] [f d7b7 d7e7] fourche deux fous. Les Noirs [m Bf6] en sauvent un, et la dame prend [m Qxb7] l'autre. [s tag b7 2.5 1-0] Lasker gagne."""),
"percee_3v3_1_fr": ("blancs", "Trois pions chacun.|Un seul gagne.",   # jumeau FR de percee_3v3_1 ; T13 B
"""[p """ + PERCEE + """] [f b5b6 a5a6 c5c6] Trois pions contre trois, et les deux rois sont loin. [h] Aux Blancs de jouer : un seul coup gagne, les autres perdent. Tu le trouves ? [q 1 Lequel ?] Abonne-toi : une astuce de finale par jour. Le pion en [m b6 brillant] [z b6 1.3 2.0] b6 ! Si les Noirs prennent avec le [m axb6] pion a, alors le pion c saute [m c6 brillant] en c6 ! Les Noirs doivent [m bxc6] reprendre, mais plus rien n'arrête le pion a. Il file [m a6] en a6. Le pion noir [m b5] court aussi, trop tard. Le [m a7] pion arrive en a7. Encore un [m b4] pas pour les Noirs, et le pion a [m a8=Q] [x impact] [z a8 1.3 2.0] devient dame ! [s tag a8 2.5 DAME] Donne deux pions pour en libérer un."""),
}
PERSO.update({k: {"cote": c, "sous_titres": "phrase", "hook": h, "script": sc, "voix": _lu(sc)} for k, (c, h, sc) in _S.items()})
QUESTIONS.update({
    "percee_3v3_1": "Would you have|found b6?",
    "lasker_bauer_1": "Would you sacrifice|both bishops?",
    "vienne_stanley_1": "Analyze your own|game, free",
    "fou_mauvaise_couleur_1": "Did you know|this draw?",
    "lasker_bauer_1_fr": "Tu aurais sacrifié|les deux fous ?",
    "percee_3v3_1_fr": "Tu aurais trouvé|b6 ?",
})

# 8/11 (Producteur) : file du Scénariste du 7/11 ; lignes vérifiées python-chess + Stockfish 16 (prof. 20-22) ; « Follow / Abonne-toi » juste avant la révélation (Simon, 3/11)
# E3 remplacé : Kieninger déjà fait en EN (pigeon_en_12, 29/10, vu par deja_fait.py --verifier) → réserve n° 20 (Bishop's Opening, prise en passant à la découverte, 2 parties Lichess ~1874)
# Rotlewi : 22.g3 n'enferme PAS la dame (22…Qe7 possible, −3,5) → « attaquée », jamais « piégée »
SHORT = "fen:4rrk1/1bpR1p1p/1pq1pQp1/p3P3/P1PR4/5N1P/2P2PP1/6K1_w_-_-_4_30"
SICIL = "fen:r2qkb1r/pp2pppp/3p1n2/1Bp1n3/4P1b1/2P2N2/PP1P1PPP/RNBQR1K1_b_kq_-_2_7"
PASSANT = "fen:r1bq1b1r/pppp1kpp/2n5/4P1N1/6n1/2Pp4/PP3PPP/RNBQK2R_b_KQ_-_2_8"
ROTLEWI = "fen:2rr2k1/1b3ppp/pb2p3/1p2P3/1P2BPnq/P1N5/1B2Q1PP/R4R1K_w_-_-_5_22"
_S = {
"short_timman_1": ("blancs", "Queen and rooks in.|What's missing?",   # Short – Timman, Tilburg 1991 : 30.h4 … 35.Kh6 (abandon) ; Stockfish +3,6 → mat en 8 après 33.Kf4 → Qg7# menacé
"""[p """ + SHORT + """] [f f6g7] Tilburg, 1991. White's queen and two rooks are already at Black's king, [h] but one piece is missing: the king itself. Can it join the attack? [q 1 Your_plan?] New story every day. Follow to get tomorrow's. The pawn [m h4] goes to h4, and Black [m h5] answers. Now the king walks to [m Kh2] h2. Black just moves [m Rc8] a rook. The king goes [m Kg3] to g3, and the rook [m Rce8] goes back. King [m Kf4 brillant] to f4! The bishop [m Bc8] retreats. And the king steps [m Kg5 brillant] [z g5 1.3 2.0] to g5, right into the enemy camp! Black [m Bxd7] takes a rook, and the king goes [m Kh6 brillant] [z h6 1.3 2.0] to h6. [f f6g7] Queen to g7 will be mate, [s tag g7 2.5 1-0] and Black resigns. Sometimes your king is your best attacker."""),
"sicilienne_dame_1": ("blancs", "Queen attacked.|Ignore it!",   # réserve n° 12 (Old Sicilian, 4 parties Lichess ~1776) : 7…Nfd7?? (7…Bd7 +0,7) 8.Nxe5! (+4,8 ; 8.d4 +0,6) … 11.Rxd1+ (+5,1)
"""[p """ + SICIL + """] [f b5e8] Sicilian. Bishop check, and Black blocks [m Nfd7 gaffe] with the knight. [h] [f b5e8] Now that knight is pinned. But White's knight is pinned too, [f g4d1] against his queen. White to move: what now? [q 1 Your_move?] Follow: one new trap every day. Knight [m Nxe5 brillant] [z e5 1.3 2.0] takes e5! His queen hangs, but who cares? Black [m Bxd1] takes her. Bishop [m Bxd7+ brillant] takes d7, check! The queen [m Qxd7] takes it. The knight takes [m Nxd7] the queen, and the king takes [m Kxd7] the knight. Now the rook [m Rxd1+] [x impact] [z d1 1.3 2.0] takes the bishop, with check. [s tag d1 2.5 +3] White gave a queen, and ends a piece up. A pinned piece defends nothing."""),
"passant_decouverte_1": ("blancs", "King in check.|Hide in the corner?",   # réserve n° 20 (Bishop's Opening, 2 parties Lichess, puzzle ~1874) : 8…Kg8?? (8…Ke8 −0,2) 9.Qb3+ d5 (seul coup) 10.exd6+ e.p. Be6 (seul coup) 11.Qxe6# ; T18 ton imagé
"""[p """ + PASSANT + """] [f g5f7] The black king is in check from the knight. [h] The corner looks like the safest room. Should he hide there? [q 1 Hide_there?] One new trap a day. Follow so you don't miss it. The king runs [m Kg8 gaffe] to the corner. It's a dead end! The queen [m Qb3+ brillant] [z b3 1.3 2.0] checks on the long diagonal. Only one shield: the pawn [m d5] jumps two squares. And now, magic: the pawn takes [m exd6+ brillant] [z d6 1.3 2.0] en passant, and the queen's check is back! The bishop [m Be6] is the last shield, and the queen [m Qxe6# mat] [x impact] [z e6 1.3 2.0] eats it. Checkmate! [s tag e6 2.5 MATE] [p """ + PASSANT + """] The safe door was the king [m Ke8 meilleur] to e8. Analyze your own game, free."""),
"rotlewi_rubinstein_1": ("noirs", "Queen attacked.|Save her?",   # Rotlewi – Rubinstein, Lodz 1907 (Wikipédia) : 22.g3 Rxc3! 23.gxh4 Rd2!! 24.Qxd2 Bxe4+ 25.Qg2 Rh3 0-1 ; Stockfish −4,4 → −6,1 → mat en 3 (Noirs)
"""[p """ + ROTLEWI + """] Lodz, 1907. White pushes [m g3 gaffe] [z h4 1.3 2.0] the pawn and attacks the black queen. [h] Rubinstein does not save her. What does he play? [q 1 Your_move?] Follow: one new chess story every day. Rook [m Rxc3 brillant] takes c3! [f b6g1 b7h1] Both bishops now aim at the white king. White [m gxh4] takes the queen. The other rook goes [m Rd2 brillant] [z d2 1.3 2.0] to d2! The queen [m Qxd2] takes it, and the bishop takes [m Bxe4+] e4, check. The [m Qg2] queen blocks, and the last rook jumps [m Rh3 brillant] [x impact] [z h3 1.3 2.0] to h3. [s tag h3 2.5 0-1] Mate is coming, and White resigns. A queen is only a piece: count the checks."""),
"short_timman_1_fr": ("blancs", "Dame et tours en place.|Qui manque ?",   # jumeau FR de short_timman_1
"""[p """ + SHORT + """] [f f6g7] Tilburg, 1991. La dame et les deux tours blanches sont déjà chez le roi noir, [h] mais il manque une pièce : le roi blanc. Peut-il rejoindre l'attaque ? [q 1 Ton_plan ?] Abonne-toi : une histoire d'échecs par jour. Le pion [m h4] va en h4, et les Noirs [m h5] répondent. Puis le roi [m Kh2] monte en h2. Les [m Rc8] Noirs bougent une tour. Le [m Kg3] roi va en g3, et la [m Rce8] tour revient. Roi en [m Kf4 brillant] f4 ! Le fou [m Bc8] recule. Et le roi file [m Kg5 brillant] [z g5 1.3 2.0] en g5, en plein camp ennemi ! Les Noirs [m Bxd7] prennent une tour, et le roi va [m Kh6 brillant] [z h6 1.3 2.0] en h6. [f f6g7] La dame en g7 fera mat, [s tag g7 2.5 1-0] et les Noirs abandonnent. Parfois, le meilleur attaquant, c'est ton roi."""),
"rotlewi_rubinstein_1_fr": ("noirs", "Dame attaquée.|Tu la sauves ?",   # jumeau FR de rotlewi_rubinstein_1
"""[p """ + ROTLEWI + """] Lodz, 1907. Les Blancs poussent [m g3 gaffe] [z h4 1.3 2.0] le pion et attaquent la dame noire. [h] Rubinstein ne la sauve pas. Que joue-t-il ? [q 1 Ton_coup ?] Abonne-toi : une histoire d'échecs par jour. La tour [m Rxc3 brillant] prend c3 ! [f b6g1 b7h1] Les deux fous visent le roi blanc. Les Blancs [m gxh4] prennent la dame. L'autre tour va [m Rd2 brillant] [z d2 1.3 2.0] en d2 ! La dame [m Qxd2] la prend, et le fou prend [m Bxe4+] e4, échec. La dame [m Qg2] s'interpose, et la dernière tour [m Rh3 brillant] [x impact] [z h3 1.3 2.0] saute en h3. [s tag h3 2.5 0-1] Le mat arrive, et les Blancs abandonnent. Une dame, ce n'est qu'une pièce : compte les échecs."""),
}
PERSO.update({k: {"cote": c, "sous_titres": "phrase", "hook": h, "script": sc, "voix": _lu(sc)} for k, (c, h, sc) in _S.items()})
QUESTIONS.update({
    "short_timman_1": "Would you walk|your king up?",
    "sicilienne_dame_1": "Would you have|saved your queen?",
    "passant_decouverte_1": "Analyze your own|game, free",
    "rotlewi_rubinstein_1": "Would you give|the queen?",
    "short_timman_1_fr": "Tu aurais fait|marcher ton roi ?",
    "rotlewi_rubinstein_1_fr": "Tu aurais donné|la dame ?",
})

# 9/11 (Producteur) : file du Scénariste du 8/11 ; lignes vérifiées python-chess + Stockfish 16 (prof. 20-28) ; « Follow / Abonne-toi » juste avant la révélation (Simon, 3/11)
# Looks variés (bois, mono, papier, ardoise, émeraude, corail) ; E2 = T23-muet (sans voix, Simon 8/11 : test du lundi) ; E4 avancé à 17 h, E2 à 21 h
CAV2 = "fen:kN1K4/p7/8/8/5N2/8/8/8_w_-_-_0_1"
OPPO = "fen:8/4k3/8/5K2/3P4/8/8/8_w_-_-_0_1"
ALBIN = "fen:rnbqk1nr/ppp2ppp/8/4P3/1bP5/4p3/PP1B1PPP/RN1QKBNR_w_KQkq_-_0_6"
RETI = "fen:rnb1kb1r/pp3ppp/2p2n2/4q3/4N3/3Q4/PPPB1PPP/2KR1BNR_b_kq_-_1_8"
_S = {
"deux_cavaliers_1": ("blancs", "Two knights.|Mate in 4?",   # composée : 1.Kc7 a5 2.Nc6 a4 3.Nd5 a3 4.Nb6# ; mat en 4 (recherche exhaustive + Stockfish 16) ; sans le pion, 3…pat (python-chess)
"""[p """ + CAV2 + """] Two knights alone can't force checkmate. [h] But here, Black has a pawn! White to move: mate in four. Can you find it? [q 1 Mate_in_4?] New puzzle every day. Follow to get tomorrow's. King to [m Kc7 brillant] [z c7 1.3 2.0] c7! A quiet move: the king takes away b7 and b8. The pawn [m a5] runs, and the knight jumps [m Nc6] to c6. The pawn runs [m a4] again. Now the other knight jumps [m Nd5] to d5. Without that pawn, this would be stalemate! But Black must push [m a3] it, and the knight lands [m Nb6# mat] [x impact] [z b6 1.4 2.0] on b6: checkmate! [s tag a8 2.5 MATE] The pawn gave White the extra move."""),
"opposition_ke5_1": ("blancs", "King and pawn.|One move wins.",   # composée : 1.Ke5! (mat en 17, Stockfish 16 prof. 32) ; Kg6, Kg5, Kg4, Kf4, Ke4, d5 = nulle (0,00 à +0,03) ; 1.d5 Kd6 0,00 ; T23-muet
"""[p """ + OPPO + """] King and pawn against king. [h] White to move. Only one move wins. Which one? [q 2 Find_it!] Follow: one new endgame every day. King to [m Ke5 brillant] [z e5 1.3 2.0] e5! Kings face to face: the opposition. Black steps [m Kd7] aside. The white king walks in [m Kd5] front of the pawn. Black waits [m Ke7] on e7. The king goes [m Kc6 brillant] to c6. Black comes [m Ke6] back. Now the pawn [m d5+] runs, with check. The king steps [m Ke5] away. The pawn goes [m d6] to d6. The king is [m Ke4] too far. The pawn goes [m d7] to d7. One last step, [m Kd3] but it's too late. The pawn [m d8=Q+] [x impact] [z d8 1.3 2.0] queens! [s tag d8 2.5 QUEEN] [p """ + OPPO + """] Push the pawn [m d5 erreur] first? The king blocks [m Kd6] it: draw. [s tag d6 2.5 DRAW] King first, pawn second."""),
"lasker_albin_1": ("blancs", "Free bishop?|Look first!",   # Albin, piège de Lasker : 6.Bxb4?? exf2+ 7.Ke2 fxg1=N+ 8.Ke1 Qh4+ 9.Kd2 Nc6 10.Qe1 Qxe1+ 11.Kxe1 Nxb4 ; Stockfish 16 : −0,1 → −6,0 ; fxg1=Q ne fait pas échec (python-chess) ; 6.fxe3 −0,1 ; T18 ton imagé
"""[p """ + ALBIN + """] [f d2b4] Albin Countergambit. Black's bishop on b4 is attacked, and nothing defends it. [h] Should White take it? [q 1 Take_it?] One new trap a day. Follow so you don't miss it. White grabs [m Bxb4 gaffe] the candy. The pawn takes [m exf2+ brillant] f2, check! The king steps to [m Ke2] e2, and the pawn becomes a [m fxg1=N+ brillant] [z g1 1.4 2.2] knight, with check! A queen would give no check here. The king runs [m Ke1] back, and the queen jumps out [m Qh4+] with check. The king goes [m Kd2] to d2, and the other knight [m Nc6] hits [f c6b4] the bishop. White offers [m Qe1] a queen trade. Black [m Qxe1+] takes, with check. The king takes [m Kxe1] back, and the knight grabs [m Nxb4] [x impact] [z b4 1.3 2.0] the bishop. [s tag b4 2.5 BLACK_WINS] Black is winning. [p """ + ALBIN + """] Better: take the [m fxe3 meilleur] pawn first. Analyze your own game, free."""),
"reti_tartakower_1": ("blancs", "Queen sacrifice.|Mate in 3.",   # Réti – Tartakower, Vienne 1910 (Edward Winter, chesshistory.com) : 8…Nxe4 9.Qd8+ Kxd8 10.Bg5++ Kc7 11.Bd8# ; Stockfish 16 mat en 3 ; 10…Ke8 11.Rd8#
"""[p """ + RETI + """] Vienna, 1910. Réti plays White, and Black grabs [m Nxe4 gaffe] a knight. [h] White to move: mate in three. Can you find it? [q 1 Mate_in_3?] New story every day. Follow to get tomorrow's. Queen to [m Qd8+ brillant] [z d8 1.4 2.0] d8, check! The king must [m Kxd8] take her. Bishop to [m Bg5+ brillant] g5: [f g5d8 d1d8] double check! The king steps [m Kc7] to c7, and the bishop goes [m Bd8# mat] [x impact] [z d8 1.4 2.0] to d8: checkmate! [s tag c7 2.5 1-0] A queen sacrifice, and a mate with a bishop. Against a double check, only the king can move."""),
"deux_cavaliers_1_fr": ("blancs", "Deux cavaliers.|Mat en 4 ?",   # jumeau FR de deux_cavaliers_1
"""[p """ + CAV2 + """] Deux cavaliers seuls ne peuvent pas forcer le mat. [h] Mais ici, les Noirs ont un pion ! Aux Blancs de jouer : mat en quatre. Tu trouves ? [q 1 Mat_en_4 ?] Abonne-toi : un défi d'échecs par jour. Le roi va [m Kc7 brillant] [z c7 1.3 2.0] en c7 ! Un coup calme : il prend les cases b7 et b8. Le pion [m a5] avance, et le cavalier saute [m Nc6] en c6. Le pion avance [m a4] encore. Puis l'autre cavalier saute [m Nd5] en d5. Sans ce pion, ce serait pat ! Mais les Noirs doivent [m a3] le pousser, et le cavalier arrive [m Nb6# mat] [x impact] [z b6 1.4 2.0] en b6 : échec et mat ! [s tag a8 2.5 MAT] Le pion a donné aux Blancs le temps qui manquait."""),
"opposition_ke5_1_fr": ("blancs", "Roi et pion.|Un seul coup gagne.",   # jumeau FR de opposition_ke5_1 (avec voix)
"""[p """ + OPPO + """] Roi et pion contre roi. [h] Aux Blancs de jouer, et un seul coup gagne. Lequel ? [q 1 Trouve-le !] Abonne-toi : un défi d'échecs par jour. Le roi va [m Ke5 brillant] [z e5 1.3 2.0] en e5 ! Les rois face à face : l'opposition. Les Noirs [m Kd7] s'écartent. Le roi blanc passe devant [m Kd5] le pion. Les Noirs attendent [m Ke7] en e7. Le roi va [m Kc6 brillant] en c6. Les Noirs [m Ke6] reviennent. Le pion file, [m d5+] avec échec. Le roi noir [m Ke5] s'écarte. Le pion va [m d6] en d6. Le roi est [m Ke4] trop loin. Le pion va [m d7] en d7. Un dernier pas, [m Kd3] mais c'est trop tard. Le pion devient [m d8=Q+] [x impact] [z d8 1.3 2.0] dame ! [s tag d8 2.5 DAME] [p """ + OPPO + """] Pousser le pion [m d5 erreur] d'abord ? Le roi noir le [m Kd6] bloque : nulle. [s tag d6 2.5 NULLE] Le roi d'abord, le pion ensuite."""),
}
PERSO.update({k: {"cote": c, "sous_titres": "phrase", "hook": h, "script": sc, "voix": _lu(sc)} for k, (c, h, sc) in _S.items()})
QUESTIONS.update({
    "deux_cavaliers_1": "Would you have|found Kc7?",
    "opposition_ke5_1": "Would you have|found Ke5?",
    "lasker_albin_1": "Analyze your own|game, free",
    "reti_tartakower_1": "Would you give|the queen?",
    "deux_cavaliers_1_fr": "Tu aurais trouvé|Rc7 ?",
    "opposition_ke5_1_fr": "Tu aurais trouvé|Re5 ?",
})
