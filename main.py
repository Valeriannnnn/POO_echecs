from Echiquier import Echiquier

if __name__ == "__main__":
    plateau = Echiquier()
    
    print("--- Test 1 : La Tour est bloquée par le Pion ---")
    # La Tour blanche est en (7,0). Le Pion blanc est en (6,0).
    # La Tour essaie d'aller en (4,0) (3 cases vers le haut).
    resultat1 = plateau.deplacer_piece(plateau.cases[7, 0], plateau.cases[4, 0])
    print("Résultat attendu : False | Obtenu :", resultat1)
    print("-" * 40)

    print("--- Test 2 : Le Cavalier saute par-dessus les pièces ---")
    # Le Cavalier blanc est en (7,1). Le Pion est en (6,1).
    # Le Cavalier saute en (5,2) (mouvement en L).
    resultat2 = plateau.deplacer_piece(plateau.cases[7, 1], plateau.cases[5, 2])
    print("Résultat attendu : True | Obtenu :", resultat2)
    print("-" * 40)

    print("--- Test 3 : La Tour passe quand le chemin est libre ---")
    # D'abord, on déplace le Pion blanc de (6,0) en (5,0) pour libérer le passage.
    plateau.deplacer_piece(plateau.cases[6, 0], plateau.cases[5, 0])
    print("(Le pion blanc en a2 a avancé en a3)")
    
    # Maintenant, la Tour essaie d'aller de (7,0) en (4,0).
    resultat3 = plateau.deplacer_piece(plateau.cases[7, 0], plateau.cases[4, 0])
    print("Résultat attendu : True | Obtenu :", resultat3)
    print("-" * 40)

    # On affiche le plateau final pour voir le résultat visuellement
    print("\nPlateau final :")
    plateau.afficher_plateau()