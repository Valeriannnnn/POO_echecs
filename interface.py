from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton

class FenetreEchecs(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mon Jeu d'Échecs")
        self.resize(600, 600)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.boutons = [[QPushButton() for _ in range(8)] for _ in range(8)]

        for ligne in range(8):
            for colonne in range(8):
                btn = self.boutons[ligne][colonne]
                btn.setFixedSize(70, 70)
                self.layout.addWidget(btn, ligne, colonne)