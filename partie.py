from Echiquier import Echiquier

class Partie:
    def __init__(self):
        self.echiquier = Echiquier()
        self.tour_actuel = "blanc"
        self.etat = "en_cours" 

    def changer_tour(self):
        self.tour_actuel = "noir" if self.tour_actuel == "blanc" else "blanc"

    def jouer_coup(self, depart, arrivee) -> bool:
        succes = self.echiquier.deplacer_piece(depart, arrivee)
        if succes:
            self.changer_tour()
            self.verifier_fin_de_partie()
        return succes

    def verifier_fin_de_partie(self):
        if self.echiquier.est_echec_et_mat(self.tour_actuel):
            self.etat = f"victoire_{'noir' if self.tour_actuel == 'blanc' else 'blanc'}"
        elif not self.echiquier.a_des_coups_legaux(self.tour_actuel):
            self.etat = "match_nul"

    def abandonner_la_partie(self):
        self.etat = f"victoire_{'noir' if self.tour_actuel == 'blanc' else 'blanc'}"

    # ==========================================
    # PARTIE TERMINAL (Console)
    # ==========================================
    def convertir_coordonnees(self, texte: str) -> tuple:
        texte = texte.strip().lower()
        if len(texte) != 2: return None, None
        if texte[0] not in "abcdefgh" or texte[1] not in "12345678": return None, None
        return 8 - int(texte[1]), ord(texte[0]) - ord('a')

    def demarrer_en_terminal(self):
        print("Bienvenue aux échecs (Mode Terminal) ! Tapez 'quitter' pour arrêter.\n")
        
        while self.etat == "en_cours":
            self.echiquier.afficher_plateau()
            print(f"Au tour des {'Blancs' if self.tour_actuel == 'blanc' else 'Noirs'}")
            
            dep_str = input("Case de départ (ex: e2) ou 'quitter' : ")
            if dep_str.lower() == 'quitter':
                break
                
            arr_str = input("Case d'arrivée (ex: e4) : ")
            
            l_dep, c_dep = self.convertir_coordonnees(dep_str)
            l_arr, c_arr = self.convertir_coordonnees(arr_str)
            
            if l_dep is None or l_arr is None:
                print("Format invalide. Réessayez.\n")
                continue
                
            depart = self.echiquier.cases[l_dep, c_dep]
            arrivee = self.echiquier.cases[l_arr, c_arr]
            
            if self.jouer_coup(depart, arrivee):
                if self.etat == "victoire_blanc":
                    self.echiquier.afficher_plateau()
                    print("ÉCHEC ET MAT ! Les Blancs ont gagné !")
                elif self.etat == "victoire_noir":
                    self.echiquier.afficher_plateau()
                    print("ÉCHEC ET MAT ! Les Noirs ont gagné !")
                elif self.etat == "match_nul":
                    self.echiquier.afficher_plateau()
                    print("PAT ! Match nul.")
            else:
                print("Déplacement invalide !\n")
