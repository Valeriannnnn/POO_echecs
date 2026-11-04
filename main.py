from Echiquier import Echiquier
from Pion import Pion

if __name__ == "__main__":
    print("=== TEST DE LA PROMOTION ===\n")
    plateau = Echiquier()

    # ---------------------------------------------------------
    print("--- Test 1 : Promotion d'un Pion BLANC ---")
    # On prépare la case (0,0) : on retire la Tour noire qui s'y trouve
    plateau.cases[0, 0].piece = None 
    # On place un Pion blanc en (1,0)
    plateau.cases[1, 0].piece = Pion("blanc", "Pion_blanc.png", plateau.cases[1, 0])
    
    print("Avant déplacement, case (1,0) :", plateau.cases[1, 0].piece)
    print("Avant déplacement, case (0,0) :", plateau.cases[0, 0].piece)

    # Le pion blanc avance en (0,0)
    plateau.deplacer_piece(plateau.cases[1, 0], plateau.cases[0, 0])
    
    print("\nAprès déplacement :")
    print("Case (1,0) :", plateau.cases[1, 0].piece) # Devrait être None
    print("Case (0,0) :", plateau.cases[0, 0].piece) # Devrait être une Dame !
    print()

    # ---------------------------------------------------------
    print("--- Test 2 : Promotion d'un Pion NOIR ---")
    # On prépare la case (7,0) : on retire la Tour blanche
    plateau.cases[7, 0].piece = None 
    # On place un Pion noir en (6,0)
    plateau.cases[6, 0].piece = Pion("noir", "Pion_noir.png", plateau.cases[6, 0])
    
    print("Avant déplacement, case (6,0) :", plateau.cases[6, 0].piece)
    
    # Le pion noir avance en (7,0)
    plateau.deplacer_piece(plateau.cases[6, 0], plateau.cases[7, 0])
    
    print("\nAprès déplacement :")
    print("Case (6,0) :", plateau.cases[6, 0].piece) # Devrait être None
    print("Case (7,0) :", plateau.cases[7, 0].piece) # Devrait être une Dame !