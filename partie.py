from Echiquier import Echiquier
from Joueur import Joueur

class Partie:
    def __init__(self, joueur1: Joueur, joueur2: Joueur):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.tour_actuel = joueur1
        self.echiquier = Echiquier()

    def changer_tour(self):
        """Passe le tour au joueur suivant."""
        if self.tour_actuel == self.joueur1:
            self.tour_actuel = self.joueur2
        else:
            self.tour_actuel = self.joueur1

    def convertir_coordonnees(self, texte: str) -> tuple:
        """
        Transforme une saisie comme 'e2' en coordonnées (ligne, colonne).
        Retourne (None, None) si l'entrée est invalide.
        """
        texte = texte.strip().lower()
        
        # On vérifie la longueur (2 caractères)
        if len(texte) != 2:
            return None, None
            
        # On vérifie que la 1ère lettre est entre 'a' et 'h'
        # et que le 2ème caractère est un chiffre entre '1' et '8'
        if texte[0] not in "abcdefgh" or texte[1] not in "12345678":
            return None, None
            
        # Si tout est bon, on calcule
        colonne = ord(texte[0]) - ord('a')
        ligne = 8 - int(texte[1])
        
        return ligne, colonne

    def demarrer(self):
        """Lance la boucle principale du jeu."""
        en_cours = True
        print("Bienvenue aux échecs ! Tapez 'quitter' pour arrêter.\n")
        
        while en_cours:
            # 1. Affichage du plateau
            self.echiquier.afficher_plateau()
            print(f"Au tour de {self.tour_actuel.name} ({self.tour_actuel.color})")
            
            # 2. Saisie utilisateur
            case_depart_str = input("Case de départ (ex: e2) ou 'quitter' : ")
            if case_depart_str.lower() == 'quitter':
                print("Partie terminée.")
                break
                
            case_arrivee_str = input("Case d'arrivée (ex: e4) : ")
            
            # 3. Conversion et vérification
            ligne_dep, col_dep = self.convertir_coordonnees(case_depart_str)
            ligne_arr, col_arr = self.convertir_coordonnees(case_arrivee_str)
            
            # Si la fonction a renvoyé None, c'est que le format était mauvais
            if ligne_dep is None or ligne_arr is None:
                print("\n❌ Format invalide. Utilisez une lettre (a-h) et un chiffre (1-8).\n")
                continue
                
            # 4. Tentative de déplacement
            case_depart = self.echiquier.cases[ligne_dep, col_dep]
            case_arrivee = self.echiquier.cases[ligne_arr, col_arr]
            
            succes = self.echiquier.deplacer_piece(case_depart, case_arrivee)
            
            # 5. Résultat
            if succes:
                self.changer_tour()
            else:
                print("\n❌ Déplacement invalide ! Réessayez.\n")
