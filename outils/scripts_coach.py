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
Fou [m Bb4 meilleur] b4 ! Tu cloues le fou contre le roi. Dame [m Qd2] d2 pour le protéger, fou prend [m Bxc3] c3, dame prend [m Qxc3] c3.
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
Les Blancs reprennent avec la dame : [m Qxd4 gaffe] dame prend d4. Erreur. Pion [m c5 bon] c5 ! La dame doit partir, [m Qd5] en d5, pour attaquer la tour a8.
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
Et maintenant : tour prend [m Rxe4 meilleur] e4 ! Le pion d5 est le seul qui bloque la colonne d. [f d1d7]
Si d prend [m dxe4] e4, la colonne s'ouvre, et dame prend [m Qxd7] d7. La dame noire tombe.
Le bon coup pour les Noirs, c'était [p e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Nxe4 d4 b5 Bb3 d5 dxe5 Be6 c3 Be7 Re1 O-O Nd4] cavalier prend [m Nxe5 meilleur] e5.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_siberien": ("noirs", """Le piège sibérien. Si on te joue le gambit Smith-Morra contre ta sicilienne, garde-le en tête.
[m e4] e4, [m c5] c5, [m d4] d4, c prend [m cxd4] d4, [m c3] c3 : les Blancs offrent un pion. d prend [m dxc3] c3, cavalier prend [m Nxc3] c3.
[p e4 c5 d4 cxd4 c3 dxc3 Nxc3 Nc6 Nf3 e6 Bc4 Qc7 O-O Nf6 Qe2] Quelques coups plus tard, les Blancs ont roqué, leur dame est en e2.
Tu joues cavalier [m Ng4 bizarre] g4. Il vise h2, [f c7h2] avec ta dame. Les Blancs le chassent : [m h3] h3.
[q 3 Trouve_le_coup_des_Noirs] Et toi, au lieu de reculer : cavalier [m Nd4 bon] d4 ! Tu attaques la dame. Les Blancs prennent : [m Nxd4 gaffe] cavalier prend d4.
Et dame [m Qh2# mat] h2. Échec et mat ! Le cavalier g4 protège ta dame.
Et s'ils avaient pris le cavalier g4, tu prenais leur dame en e2, avec échec.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_kieninger": ("noirs", """Le piège Kieninger, dans le gambit de Budapest.
[m d4] d4, cavalier [m Nf6] f6, [m c4] c4, [m e5 bizarre] e5 ! d prend [m dxe5] e5, cavalier [m Ng4] g4 : tu vas récupérer le pion.
Fou [m Bf4] f4, cavalier [m Nc6] c6, cavalier [m Nf3] f3, fou [m Bb4+] b4, échec, cavalier [m Nbd2] d2, dame [m Qe7] e7.
Les Blancs chassent ton fou : [m a3] a3. Et tu reprends le pion, cavalier prend [m Ngxe5 bon] e5, en laissant ton fou !
Les Blancs le prennent : [m axb4 gaffe] a prend b4. Et cavalier [m Nd3# mat] d3. Échec et mat !
Le pion e2 pourrait prendre… mais il est cloué par ta dame. [f e7e1]
Le bon coup, c'était [p d4 Nf6 c4 e5 dxe5 Ng4 Bf4 Nc6 Nf3 Bb4+ Nbd2 Qe7 a3 Ngxe5] cavalier prend [m Nxe5 meilleur] e5.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_foiefrit": ("blancs", """L'attaque du foie frit. Une des attaques les plus connues sur Internet.
[m e4] e4, [m e5] e5, cavalier [m Nf3] f3, cavalier [m Nc6] c6, fou [m Bc4] c4, cavalier [m Nf6] f6.
Cavalier [m Ng5 bizarre] g5 ! Tu vises f7 [f g5f7 c4f7] avec deux pièces. Les Noirs bloquent : [m d5] d5, e prend [m exd5] d5.
Et beaucoup reprennent avec le cavalier : [m Nxd5 erreur] cavalier prend d5. C'est là que tu sacrifies.
Cavalier prend [m Nxf7 bon] f7 ! Le roi [m Kxf7] prend, dame [m Qf3+] f3, échec. Le roi monte [m Ke6] en e6 pour protéger son cavalier.
Cavalier [m Nc3] c3 : tu attaques le cavalier cloué, et le roi noir est au milieu de l'échiquier. Ça, c'est le foie frit.
Pour les Noirs, le bon coup était [p e4 e5 Nf3 Nc6 Bc4 Nf6 Ng5 d5 exd5] cavalier [m Na5 meilleur] a5.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_tennison": ("blancs", """Le gambit Tennison. Peu de gens le connaissent, et c'est pour ça qu'il marche.
Cavalier [m Nf3] f3, [m d5] d5, [m e4 bizarre] e4 ! Tu donnes un pion. d prend [m dxe4] e4, cavalier [m Ng5] g5 : tu vas le récupérer.
Cavalier [m Nf6] f6, [m d3] d3, e prend [m exd3] d3, fou prend [m Bxd3] d3.
Les Noirs veulent chasser ton cavalier : [m h6 gaffe] h6. Erreur. Cavalier prend [m Nxf7 bon] f7 ! Le roi [m Kxf7] prend… et fou [m Bg6+ meilleur] g6, échec !
Si le roi prend [m Kxg6] le fou, dame prend [m Qxd8] d8. La colonne d s'est ouverte, et la dame noire tombe.
Le bon coup pour les Noirs, c'était [p Nf3 d5 e4 dxe4 Ng5 Nf6 d3 exd3 Bxd3] cavalier [m Nc6 meilleur] c6.
Analyse tes parties gratuitement sur BlunderCheck."""),

"v_halosar": ("blancs", """Le piège Halosar, dans le gambit Blackmar-Diemer.
[m d4] d4, [m d5] d5, [m e4 bizarre] e4 ! d prend [m dxe4] e4, cavalier [m Nc3] c3, cavalier [m Nf6] f6, [m f3] f3, e prend [m exf3] f3, dame prend [m Qxf3] f3.
Les Noirs prennent un deuxième pion : dame prend [m Qxd4] d4. Fou [m Be3] e3, dame [m Qb4] b4, et grand roque [m O-O-O] : ta tour arrive sur la colonne d.
Les Noirs attaquent ta dame : fou [m Bg4 gaffe] g4. Et toi, tu la laisses ! Cavalier [m Nb5 meilleur] b5 ! [f b5c7]
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
}
# ---------- question affichée sur les dernières secondes (pousse aux commentaires) ----------
QUESTIONS = {}
QUESTION_DEFAUT = "Tu l'aurais vu ?|Réponds en commentaire."
