# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 14:57:56 2026

@author: valer
"""
from Piece import Piece

class Roi(Piece):
    
    # Attributs spécifiques au Roi
    a_deja_bouger: bool
    
    def __init__(self, couleur: str, cheminImage: str, position: "Case"= None):
        # On appelle le constructeur de Piece (super)
        super().__init__(couleur, cheminImage, position)
        
        # On initialise l'attribut spécifique
        self.a_deja_bouger = False
        
    def se_Deplacer(self, case_cible: "Case") -> bool:
        """
        Vérifie si le Roi peut se déplacer.
        """
        #La pièce connaît déjà sa position actuelle
        depart = self.position
        
        #Calcul de la distance (on garde la direction)
        diff_ligne = case_cible.ligne - depart.ligne
        diff_colonne = case_cible.colonne - depart.colonne
       
        #On refuse le sur place
        if diff_ligne == 0 and diff_colonne == 0:
            return False
           
        #On vérifie la distance en absolue
        if abs(diff_ligne) <= 1 and abs(diff_colonne) <= 1:
            return True
       
        return False