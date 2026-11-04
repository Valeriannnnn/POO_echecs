from Echiquier import Echiquier
from Fou import Fou
from Cavalier import Cavalier

if __name__ == "__main__":
    print("=== TEST DU CLOUAGE (Coup suicidaire) ===\n")
    plateau = Echiquier()
    
    # On nettoie la colonne e (fichier e) pour l'exemple
    # On met un Fou noir en e8 (0,4)
    plateau.cases[0, 4].piece = Fou("noir", "Fou_noir.png", plateau.cases[0, 4])
    
    # On met un Cavalier blanc en e4 (4,4)
    plateau.cases[4, 4].piece = Cavalier("blanc", "Cavalier_blanc.png", plateau.cases[4, 4])
    
    # On enlève les pièces entre le Roi blanc (e1) et le Cavalier (e4)
    plateau.cases[5, 4].piece = None
    plateau.cases[6, 4].piece = None
    
    # Vérifions l'état
    print("Le Roi blanc est en échec ?", plateau.est_en_echec("blanc")) # False, le Cavalier bloque
    
    print("\nLe Cavalier blanc essaie de bouger (vers d2). C'est illégal car il expose son Roi !")
    succes = plateau.deplacer_piece(plateau.cases[4, 4], plateau.cases[6, 3]) # Le cavalier va en d2
    print("Résultat attendu : False | Obtenu :", succes)
    
    print("\nLe Cavalier est-il resté en e4 ?", plateau.cases[4, 4].piece) # True, il n'a pas pu bouger