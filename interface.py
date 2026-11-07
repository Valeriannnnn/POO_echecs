from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout)
from Partie import Partie

Icones_Pieces = {
    ("blanc", "Roi"): "♔", ("blanc", "Dame"): "♕", ("blanc", "Tour"): "♖",
    ("blanc", "Fou"): "♗", ("blanc", "Cavalier"): "♘", ("blanc", "Pion"): "♙",
    ("noir", "Roi"): "♚", ("noir", "Dame"): "♛", ("noir", "Tour"): "♜",
    ("noir", "Fou"): "♝", ("noir", "Cavalier"): "♞", ("noir", "Pion"): "♟",
}

class FenetreEchecs(QWidget):
    """
    Fenêtre PyQt5 du jeu d'échecs.

    Affiche le plateau sous forme d'une grille de 8 x 8 boutons, avec un
    bouton d'abandon. Le titre de la fenêtre indique à qui c'est le tour.

    Attributes
    ----------
    partie : Partie
        Partie en cours.
    case_selectionnee : tuple of int or None
        Ligne et colonne de la case sélectionnée, None si aucune ne l'est.
    boutons : list of list of QPushButton
        Boutons du plateau, indexés par [ligne][colonne].
    """


    def __init__(self):
        super().__init__()
        self.resize(600, 700)

        self.partie = Partie()
        self.setWindowTitle("Au tour des Blancs")
        self.case_selectionnee = None 

        self.layout_principal = QVBoxLayout()
        self.setLayout(self.layout_principal)

        self.layout_grille = QGridLayout()
        self.layout_principal.addLayout(self.layout_grille)

        self.boutons = [[QPushButton() for _ in range(8)] for _ in range(8)]
        for ligne in range(8):
            for colonne in range(8):
                btn = self.boutons[ligne][colonne]
                btn.setFixedSize(70, 70)
                btn.clicked.connect(lambda checked, l=ligne, c=colonne: self.clic_case(l, c))
                self.layout_grille.addWidget(btn, ligne, colonne)

        # bouton abandonner
        self.layout_boutons = QHBoxLayout()
        self.layout_principal.addLayout(self.layout_boutons)

        self.btn_abandonner = QPushButton("Abandonner")
        self.btn_abandonner.setFixedHeight(40)
        self.btn_abandonner.clicked.connect(self.action_abandonner)
        self.layout_boutons.addWidget(self.btn_abandonner)

        self.mettre_a_jour_affichage()


    def mettre_a_jour_affichage(self):
        """
        Redessine les pièces et les couleurs des cases.

        La surbrillance de la case sélectionnée est effacée.
        """
        for ligne in range(8):
            for colonne in range(8):
                piece = self.partie.echiquier.cases[ligne, colonne].piece
                btn = self.boutons[ligne][colonne]
                
                if piece is None:
                    btn.setText("")
                else:
                    symbole = Icones_Pieces.get((piece.couleur, piece.__class__.__name__), "?")
                    btn.setText(symbole)
                
                if (ligne + colonne) % 2 == 0:
                    btn.setStyleSheet("background-color: #F0D9B5; font-size: 40px;")
                else:
                    btn.setStyleSheet("background-color: #B58863; font-size: 40px;")


    def clic_case(self, ligne, colonne):
        """
        Gère le clic sur une case du plateau.

        Un premier clic sélectionne une pièce du joueur dont c'est le tour.
        Le clic suivant tente de la déplacer vers la case cliquée. Si le coup
        est refusé, il sélectionne la pièce cliquée si elle appartient à ce
        joueur, sinon il annule la sélection. Le clic est ignoré si la partie
        est terminée.

        Parameters
        ----------
        ligne : int
            Ligne de la case cliquée, de 0 (en haut) à 7.
        colonne : int
            Colonne de la case cliquée, de 0 (à gauche) à 7.
        """
        if self.partie.etat != "en_cours": return 

        piece_cliquee = self.partie.echiquier.cases[ligne, colonne].piece

        if self.case_selectionnee is None:
            if piece_cliquee is not None and piece_cliquee.couleur == self.partie.tour_actuel:
                self.case_selectionnee = (ligne, colonne)
                self.mettre_a_jour_affichage()
                self.boutons[ligne][colonne].setStyleSheet("background-color: yellow; font-size: 40px;")
        else:
            ligne_dep, col_dep = self.case_selectionnee
            depart = self.partie.echiquier.cases[ligne_dep, col_dep]
            arrivee = self.partie.echiquier.cases[ligne, colonne]
            
            succes = self.partie.jouer_coup(depart, arrivee)
            
            if succes:
                titre = "Au tour des Blancs" if self.partie.tour_actuel == "blanc" else "Au tour des Noirs"
                self.setWindowTitle(titre)
                self.case_selectionnee = None
                self.mettre_a_jour_affichage()
                self.verifier_fin_de_partie()
            else:
                if piece_cliquee is not None and piece_cliquee.couleur == self.partie.tour_actuel:
                    self.case_selectionnee = (ligne, colonne)
                    self.mettre_a_jour_affichage()
                    self.boutons[ligne][colonne].setStyleSheet("background-color: yellow; font-size: 40px;")
                else:
                    self.case_selectionnee = None
                    self.mettre_a_jour_affichage()


    def verifier_fin_de_partie(self):
        """Annonce le résultat et ferme la fenêtre si la partie est terminée."""
        if self.partie.etat == "victoire_blanc":
            QMessageBox.information(self, "Fin de partie", "ÉCHEC ET MAT !\nLes Blancs ont gagné !")
            self.close()
        elif self.partie.etat == "victoire_noir":
            QMessageBox.information(self, "Fin de partie", "ÉCHEC ET MAT !\nLes Noirs ont gagné !")
            self.close()
        elif self.partie.etat == "match_nul":
            QMessageBox.information(self, "Fin de partie", "PAT ! Match nul.")
            self.close()


    def action_abandonner(self):
        """
        Fait abandonner le joueur dont c'est le tour, après confirmation.

        Si le joueur confirme, annonce le gagnant et ferme la fenêtre.
        """
        reponse = QMessageBox.question(self, "Abandon", "Voulez-vous vraiment abandonner ?", 
                                       QMessageBox.Yes | QMessageBox.No)
        if reponse == QMessageBox.Yes:
            self.partie.abandonner_la_partie() 
            gagnant = "Noirs" if self.partie.tour_actuel == "blanc" else "Blancs"
            QMessageBox.information(self, "Abandon", f"Les {gagnant} gagnent par abandon.")
            self.close()
        