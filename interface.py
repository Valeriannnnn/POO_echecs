from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QMessageBox
from Echiquier import Echiquier

# Dictionnaire pour afficher les symboles des pièces
Icones_Pieces = {
    ("blanc", "Roi"): "♔", ("blanc", "Dame"): "♕", ("blanc", "Tour"): "♖",
    ("blanc", "Fou"): "♗", ("blanc", "Cavalier"): "♘", ("blanc", "Pion"): "♙",
    ("noir", "Roi"): "♚", ("noir", "Dame"): "♛", ("noir", "Tour"): "♜",
    ("noir", "Fou"): "♝", ("noir", "Cavalier"): "♞", ("noir", "Pion"): "♟",
}

class FenetreEchecs(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Au tour des Blancs")
        self.resize(600, 600)

        # On instancie la logique du jeu
        self.echiquier = Echiquier()
        
        # Variables pour gérer les tours et la sélection
        self.tour_actuel = "blanc"
        self.case_selectionnee = None 

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.boutons = [[QPushButton() for _ in range(8)] for _ in range(8)]

        for ligne in range(8):
            for colonne in range(8):
                btn = self.boutons[ligne][colonne]
                btn.setFixedSize(70, 70)
                # On connecte le clic à la méthode clic_case
                btn.clicked.connect(lambda checked, l=ligne, c=colonne: self.clic_case(l, c))
                self.layout.addWidget(btn, ligne, colonne)

        # On affiche les pièces au démarrage
        self.mettre_a_jour_affichage()

    def mettre_a_jour_affichage(self):
        """Met à jour les couleurs et le texte de chaque bouton."""
        for ligne in range(8):
            for colonne in range(8):
                piece = self.echiquier.cases[ligne, colonne].piece
                btn = self.boutons[ligne][colonne]
                
                if piece is None:
                    btn.setText("")
                else:
                    # Utilisation du nouveau nom de dictionnaire
                    symbole = Icones_Pieces.get((piece.couleur, piece.__class__.__name__), "?")
                    btn.setText(symbole)
                
                # Couleurs du damier
                if (ligne + colonne) % 2 == 0:
                    btn.setStyleSheet("background-color: #F0D9B5; font-size: 40px;")
                else:
                    btn.setStyleSheet("background-color: #B58863; font-size: 40px;")

    def clic_case(self, ligne, colonne):
        piece_cliquee = self.echiquier.cases[ligne, colonne].piece

        # CAS 1 : Sélection d'une pièce
        if self.case_selectionnee is None:
            if piece_cliquee is not None and piece_cliquee.couleur == self.tour_actuel:
                self.case_selectionnee = (ligne, colonne)
                self.mettre_a_jour_affichage()
                # La case sélectionnée devient jaune
                self.boutons[ligne][colonne].setStyleSheet("background-color: yellow; font-size: 40px;")
        
        # CAS 2 : Tentative de déplacement
        else:
            ligne_dep, col_dep = self.case_selectionnee
            depart = self.echiquier.cases[ligne_dep, col_dep]
            arrivee = self.echiquier.cases[ligne, colonne]
            
            succes = self.echiquier.deplacer_piece(depart, arrivee)
            
            if succes:
                # Changement de tour
                self.tour_actuel = "noir" if self.tour_actuel == "blanc" else "blanc"
                titre = "Au tour des Blancs" if self.tour_actuel == "blanc" else "Au tour des Noirs"
                self.setWindowTitle(titre)
                
                self.case_selectionnee = None
                self.mettre_a_jour_affichage()
                
                # On vérifie si la partie est finie
                self.verifier_fin_de_partie()
                
            else:
                # Si on clique sur une autre de nos pièces, on change la sélection
                if piece_cliquee is not None and piece_cliquee.couleur == self.tour_actuel:
                    self.case_selectionnee = (ligne, colonne)
                    self.mettre_a_jour_affichage()
                    self.boutons[ligne][colonne].setStyleSheet("background-color: yellow; font-size: 40px;")
                else:
                    # Sinon on annule la sélection
                    self.case_selectionnee = None
                    self.mettre_a_jour_affichage()

    def verifier_fin_de_partie(self):
        """Détecte l'échec et mat ou le pat et affiche le résultat."""
        if self.echiquier.est_echec_et_mat(self.tour_actuel):
            gagnant = "Noirs" if self.tour_actuel == "blanc" else "Blancs"
            QMessageBox.information(self, "Échec et Mat", f"ÉCHEC ET MAT !\nLes {gagnant} ont gagné !")
            self.close()
        elif not self.echiquier.a_des_coups_legaux(self.tour_actuel):
            QMessageBox.information(self, "Pat", "PAT ! Match nul, plus aucun coup possible.")
            self.close()
        