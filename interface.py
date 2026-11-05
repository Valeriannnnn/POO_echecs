from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton
from Echiquier import Echiquier


Icones_Pieces = {
    ("blanc", "Roi"): "♔", ("blanc", "Dame"): "♕", ("blanc", "Tour"): "♖",
    ("blanc", "Fou"): "♗", ("blanc", "Cavalier"): "♘", ("blanc", "Pion"): "♙",
    ("noir", "Roi"): "♚", ("noir", "Dame"): "♛", ("noir", "Tour"): "♜",
    ("noir", "Fou"): "♝", ("noir", "Cavalier"): "♞", ("noir", "Pion"): "♟",
}
class FenetreEchecs(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jeu d'échecs")
        self.resize(600, 600)

        # On met en place l'échiquier et les boutons
        self.echiquier = Echiquier()

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.boutons = [[QPushButton() for _ in range(8)] for _ in range(8)]

        for ligne in range(8):
            for colonne in range(8):
                btn = self.boutons[ligne][colonne]
                btn.setFixedSize(70, 70)
                self.layout.addWidget(btn, ligne, colonne)

        # On met à jour l'affichage pour voir les pièces au démarrage
        self.mettre_a_jour_affichage()

    def mettre_a_jour_affichage(self):
        """Met à jour les couleurs et le texte de chaque bouton."""
        for ligne in range(8):
            for colonne in range(8):
                piece = self.echiquier.cases[ligne, colonne].piece
                btn = self.boutons[ligne][colonne]
                
                # Gestion des pièces
                if piece is None:
                    btn.setText("")
                else:
                    symbole = Icones_Pieces.get((piece.couleur, piece.__class__.__name__), "?")
                    btn.setText(symbole)
                
                # Gestion des couleurs (damier clair / foncé) et de la taille des pièces
                if (ligne + colonne) % 2 == 0:
                    btn.setStyleSheet("background-color: #F0D9B5; font-size: 40px;")
                else:
                    btn.setStyleSheet("background-color: #B58863; font-size: 40px;")