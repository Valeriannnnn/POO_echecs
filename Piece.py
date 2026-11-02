# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:47:09 2026

@author: valer
"""

class Piece:
    #Attributs
    couleur: str
    position: "Case"
    cheminImage: str
    
    def __init__(self, couleur: str, cheminImage: str, position: "Case" = None):
        self.couleur = couleur
        self.position = position
        self.cheminImage = cheminImage
    
    def getCouleur(self):
        
        """
        Permet d'obtenir la couleur.
        
        Return:
            str: La couleur du pion sélectionné
        """
        pass
    
    def se_Deplacer(self, case_cible: "Case") -> bool:
        
        """
        Permet de déplacer une pièce
        
        Returns:
            bool: Est-ce que le déplacement est autorisé ?
        """
        
        pass