import sys
from PyQt5.QtWidgets import QApplication
from interface import FenetreEchecs
from Partie import Partie

if __name__ == "__main__":
    print("=== MON JEU D'ECHECS ===")
    print("1 - Jouer avec l'interface graphique")
    print("2 - Jouer dans le terminal")
    
    choix = input("Votre choix (1 ou 2) : ")
    print("")

    if choix == "1":
        app = QApplication(sys.argv)
        fenetre = FenetreEchecs()
        fenetre.show()
        sys.exit(app.exec_())
        
    elif choix == "2":
        ma_partie = Partie()
        ma_partie.demarrer_en_terminal()
        
    else:
        print("Choix invalide. Fermeture du programme.")