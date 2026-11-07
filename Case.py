class Case:
    """
    Case de l'échiquier.

    Parameters
    ----------
    ligne : int
        Indice de la ligne, de 0 (en haut) à 7.
    colonne : int
        Indice de la colonne, de 0 (à gauche) à 7.

    Attributes
    ----------
    piece : Piece or None
        Pièce posée sur la case, None si la case est vide.
    """
    
    def __init__(self, ligne:int, colonne: int):
        self.ligne = ligne
        self.colonne = colonne
        #A la création, la case est vide (elle ne contient aucune pièce)
        self.piece = None
            
            
    def est_vide(self) -> bool:
        """
        Vérifie si la case est vide.

        Returns
        -------
        bool
            True si la case ne contient aucune pièce, False sinon.
        """ 
        return self.piece is None
    
    