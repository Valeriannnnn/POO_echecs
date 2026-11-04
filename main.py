from Echiquier import Echiquier

if __name__ == "__main__":
    print("=== TEST DU ROQUE ===\n")

    # ---------------------------------------------------------
    print("--- Test 1 : Le Petit Roque (côté Roi) ---")
    plateau = Echiquier()
    
    # On libère le chemin pour le petit roque blanc (on retire le Fou et le Cavalier)
    plateau.cases[7, 5].piece = None # Fou en f1
    plateau.cases[7, 6].piece = None # Cavalier en g1
    
    # Le Roi va de e1 (7,4) à g1 (7,6)
    succes = plateau.deplacer_piece(plateau.cases[7, 4], plateau.cases[7, 6])
    print("Résultat attendu : True | Obtenu :", succes)
    
    # Vérifions que la Tour a bien bougé en f1 (7,5)
    tour_f1 = plateau.cases[7, 5].piece
    print("La Tour est-elle en f1 ? :", tour_f1 is not None and tour_f1.__class__.__name__ == "Tour")
    print()

    # ---------------------------------------------------------
    print("--- Test 2 : Le Grand Roque (côté Dame) ---")
    plateau = Echiquier()
    
    # On libère le chemin pour le grand roque blanc (on retire Cavalier, Fou et Dame)
    plateau.cases[7, 1].piece = None # Cavalier en b1
    plateau.cases[7, 2].piece = None # Fou en c1
    plateau.cases[7, 3].piece = None # Dame en d1
    
    # Le Roi va de e1 (7,4) à c1 (7,2)
    succes = plateau.deplacer_piece(plateau.cases[7, 4], plateau.cases[7, 2])
    print("Résultat attendu : True | Obtenu :", succes)
    
    # Vérifions que la Tour a bien bougé en d1 (7,3)
    tour_d1 = plateau.cases[7, 3].piece
    print("La Tour est-elle en d1 ? :", tour_d1 is not None and tour_d1.__class__.__name__ == "Tour")
    print()

    # ---------------------------------------------------------
    print("--- Test 3 : Le Roque est interdit si le chemin est bloqué ---")
    plateau = Echiquier()
    
    # On ne retire AUCUNE pièce. Le Cavalier et le Fou sont toujours là.
    # Le Roi essaie de faire le petit roque.
    succes = plateau.deplacer_piece(plateau.cases[7, 4], plateau.cases[7, 6])
    print("Résultat attendu : False | Obtenu :", succes)
    print()

    # ---------------------------------------------------------
    print("--- Test 4 : Le Roque est interdit si le Roi a déjà bougé ---")
    plateau = Echiquier()
    
    # On libère le chemin
    plateau.cases[7, 5].piece = None
    plateau.cases[7, 6].piece = None
    
    # On déplace le Roi de e1 vers f1 (7,5) puis on le remet en e1 (7,4)
    plateau.deplacer_piece(plateau.cases[7, 4], plateau.cases[7, 5])
    plateau.deplacer_piece(plateau.cases[7, 5], plateau.cases[7, 4])
    
    # On essaie maintenant de faire le petit roque
    succes = plateau.deplacer_piece(plateau.cases[7, 4], plateau.cases[7, 6])
    print("Résultat attendu : False (Le Roi a déjà bougé) | Obtenu :", succes)