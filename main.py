from Echiquier import Echiquier

if __name__ == "__main__":
    print("=== TEST DU MAT DU BERGER ===\n")
    plateau = Echiquier()
    
    # 1. e4 (blanc) / e5 (noir)
    plateau.deplacer_piece(plateau.cases[6, 4], plateau.cases[4, 4])
    plateau.deplacer_piece(plateau.cases[1, 4], plateau.cases[3, 4])
    
    # 2. Fc4 (blanc) / Cc6 (noir)
    # Le Fou va en (4,2) pour protéger la Dame plus tard
    plateau.deplacer_piece(plateau.cases[7, 5], plateau.cases[4, 2])
    plateau.deplacer_piece(plateau.cases[0, 1], plateau.cases[2, 2])
    
    # 3. Dh5 (blanc) / Cf6 (noir, l'erreur fatale)
    plateau.deplacer_piece(plateau.cases[7, 3], plateau.cases[3, 7])
    plateau.deplacer_piece(plateau.cases[0, 6], plateau.cases[2, 5])
    
    # 4. Dxf7# (La Dame blanche mange en f7)
    succes = plateau.deplacer_piece(plateau.cases[3, 7], plateau.cases[1, 5])
    print("Coup final joué :", succes)
    
    print("\n--- Analyse de la position ---")
    print("Le Roi noir est en échec ?", plateau.est_en_echec("noir")) 
    print("Le Roi noir a des coups légaux ?", plateau.a_des_coups_legaux("noir")) 
    print("EST-CE ÉCHEC ET MAT ?", plateau.est_echec_et_mat("noir")) 