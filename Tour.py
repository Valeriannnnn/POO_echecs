# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:21:14 2026

@author: valer
"""

from Piece import Piece

class Tour(Piece):
    
    #Attributs spécifique a la tour
    a_deja_bouger: bool
    
    def __init__(self, couleur: str, cheminImage: str, position: "Case"= None):
        #On appelle le constructeur de Piece (super)
        super().__init__(couleur, cheminImage, position)
        
        #On initialise l'attribut spécifique
        self.a_deja_bouger = False
        
    def se_Deplacer(self, case_cible: "Case") -> bool:
        """
        Vérifie si la Tour peut se déplacer.

        Parameters
        ----------
        case_cible : Case
            Correspond à la case que le joueur a cliqué.

        Returns
        -------
        bool
            Est-ce que la tour peut se déplacer ?
        """
        
        