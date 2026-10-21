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
