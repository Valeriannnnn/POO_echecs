# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:25:36 2026

@author: valer
"""

from Piece import Piece

class Cavalier(Piece):
    
    def __init__(self, couleur: str, cheminImage: str, position: "Case"= None):
        #On appelle le constructeur de Piece (super)
        super().__init__(couleur, cheminImage, position)
        
        
    def se_Deplacer(self, case_cible: "Case") -> bool:
        """
        Vérifie si le cavalier peut se déplacer.

        Parameters
        ----------
        case_cible : Case
            Correspond à la case que le joueur a cliqué.

        Returns
        -------
        bool
            Est-ce que le cavalier peut se déplacer ?
        """
        
        #La pièce connaît déjà sa position actuelle
        depart = self.position
        
        #Calcul de la distance (on garde la direction)
        diff_ligne = case_cible.ligne - depart.ligne
        diff_colonne = case_cible.colonne - depart.colonne
        
        if abs(diff_ligne)==2 and abs(diff_colonne)==1:
            return True
        
        if abs(diff_colonne)==2 and abs(diff_ligne)==1:
            return True
        
        return False