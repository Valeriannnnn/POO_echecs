from Echiquier import Echiquier

if __name__ == "__main__":
    print("--- 1. Affichage du plateau de départ ---")
    plateau = Echiquier()
    plateau.afficher_plateau()

    print("\n--- 2. On tente de déplacer le Pion blanc de e2 vers e4 ---")
    # Sur notre échiquier, e2 c'est la ligne 6, colonne 4. e4 c'est la ligne 4, colonne 4.
    case_depart = plateau.cases[6, 4]
    case_arrivee = plateau.cases[4, 4]
    
    succes = plateau.deplacer_piece(case_depart, case_arrivee)
    
    if succes:
        print("✅ Déplacement réussi !")
    else:
        print("❌ Déplacement refusé.")

    print("\n--- 3. Affichage du plateau après le déplacement ---")
    plateau.afficher_plateau()