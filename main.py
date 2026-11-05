import sys
from PyQt5.QtWidgets import QApplication
from interface import FenetreEchecs

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = FenetreEchecs()
    fenetre.show()
    sys.exit(app.exec_())