class Case:
    #Attributs
    ligne: int
    colonne: int
    piece: "Piece" # On met des guillemets pour éviter l'import circulaire
    
    def __init__(self, ligne:int, colonne: int):
        self.ligne = ligne
        self.colonne = colonne
        #A la création, la case est vide (elle ne contient aucune pièce)
        self.piece = None
            
            
    def est_vide(self) -> bool:
        
        """
        Vérifie si la case est vide.
        
        Returns:
            bool: True si la case ne contient aucune pièce, False sinon.
        """
        
        return self.piece is None
    
    