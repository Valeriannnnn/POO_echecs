README

# POO_echecs - Jeu d'échecs en Python
Projet du cours d'analyse informatique et POO (PPMD, 2026).
Deux joueurs sur le même poste, en fenêtre PyQt5 ou dans le terminal.

## INSTALLATION
    python -m pip install numpy PyQt5
    (testé avec Python 3.15, numpy 2.5 et PyQt5 5.15)

## LANCEMENT
    python main.py        (depuis ce dossier)
Taper 1 pour la fenêtre, 2 pour le terminal.
- Fenêtre : cliquer sur une pièce, puis sur la case d'arrivée.
- Terminal : saisir la case de départ, puis celle d'arrivée (e2, e4).
  « quitter » arrête la partie. Blancs en majuscules, Noirs en minuscules.

## FICHIERS
    main.py          menu de lancement
    interface.py     fenêtre PyQt5
    Partie.py        tours, fin de partie, mode terminal
    Echiquier.py     plateau, coups, échec, mat, roque, promotion
    Case.py          case du plateau
    Piece.py         classe mère de Roi, Dame, Tour, Fou, Cavalier et Pion
    Diagrammes UML avant implémentation/    analyse et conception

## RÈGLES GÉRÉES
Déplacements, prises, échec, mat, pat, roque, promotion.
Abandon dans la fenêtre uniquement.

## LIMITES DU JEU
- promotion en dame uniquement.
- Le pat est le seul cas de partie nulle.

REMARQUES SUR LA CONSTRUCTION DU JEU

1: On choisit de ne pas reproduire certains diagrammes, comme par exemple le diagramme d’activité de la configuration du jeu car le jeu se lance quasiment directement. Il y a juste à choisir entre jouer dans le terminal ou avec l’interface. J’ai fait ce choix car je n’ai finalement pas mis les différentes contraintes tel que le chronomètre ou les différents niveaux de PNJ par manque de temps. Le jeu est donc finalement un simple 1 vs 1 entre deux vrais joueurs.

2: On a aussi retiré les diagrammes de séquences car on considérait le diagramme d’état-transition et le diagramme d’activité suffisant pour expliquer le déroulé du jeu.
