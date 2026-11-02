# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:26:27 2026

@author: valer
"""

from Piece import Piece

class Dame(Piece):
    
    def __init__(self, couleur: str, cheminImage: str, position: "Case"= None):
        #On appelle le constructeur de Piece (super)
        super().__init__(couleur, cheminImage, position)
        
        
    def se_Deplacer(self, case_cible: "Case") -> bool:
        """
        Vérifie si la dame peut se déplacer.

        Parameters
        ----------
        case_cible : Case
            Correspond à la case que le joueur a cliqué.

        Returns
        -------
        bool
            Est-ce que la dame peut se déplacer ?
        """
        
        pass