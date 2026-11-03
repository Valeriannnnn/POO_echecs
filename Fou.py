# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:24:21 2026

@author: valer
"""

from Piece import Piece

class Fou(Piece):
    
    def __init__(self, couleur: str, cheminImage: str, position: "Case"= None):
        #On appelle le constructeur de Piece (super)
        super().__init__(couleur, cheminImage, position)
        
        
    def se_Deplacer(self, case_cible: "Case") -> bool:
        """
        Vérifie si le Fou peut se déplacer (en diagonale).
        """
        depart = self.position
        
        diff_ligne = case_cible.ligne - depart.ligne
        diff_colonne = case_cible.colonne - depart.colonne
        
        # On refuse le sur place
        if diff_ligne == 0 and diff_colonne == 0:
            return False
            
        # Mouvement diagonal (distance absolue identique sur les deux axes)
        if abs(diff_ligne) == abs(diff_colonne):
            return True
            
        return False