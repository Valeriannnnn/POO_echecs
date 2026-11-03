from Echiquier import Echiquier

if __name__ == "__main__":
    # On crée l'échiquier
    plateau = Echiquier()
    
    # On affiche le plateau de départ
    print("--- Plateau de départ ---")
    plateau.afficher_plateau()

    # On fait nos tests
    print("--- Tests de la Dame ---")
    print("1. Pion devant la Dame (déplacement) :", plateau.deplacer_piece(plateau.cases[6, 3], plateau.cases[4, 3]))
    print("2. Dame en ligne :", plateau.deplacer_piece(plateau.cases[7, 3], plateau.cases[5, 3]))
    print("3. Dame en diagonale :", plateau.deplacer_piece(plateau.cases[5, 3], plateau.cases[3, 5]))
    print("4. Dame en L :", plateau.deplacer_piece(plateau.cases[3, 5], plateau.cases[1, 4]))

    # On affiche le résultat final
    print("--- Plateau après les tests ---")
    plateau.afficher_plateau()