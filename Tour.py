# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:21:14 2026

@author: valer
"""

from Piece import Piece

class Tour(Piece):
    
    #Attributs spécifique a la tour
    a_deja_bouger: bool
    
    def __init__(self, couleur: str, position: "Case"= None):
        #On appelle le constructeur de Piece (super)
        super().__init__(couleur, position)
        
        #On initialise l'attribut spécifique
        self.a_deja_bouger = False
        
    def se_Deplacer(self, case_cible: "Case") -> bool:
        """
        Vérifie si la Tour peut se déplacer (en ligne droite).
        """
        depart = self.position
        
        diff_ligne = case_cible.ligne - depart.ligne
        diff_colonne = case_cible.colonne - depart.colonne
        
        # On refuse le sur place
        if diff_ligne == 0 and diff_colonne == 0:
            return False
            
        # Mouvement horizontal (même ligne) ou vertical (même colonne)
        if diff_ligne == 0 or diff_colonne == 0:
            return True
            
        return False
        
        