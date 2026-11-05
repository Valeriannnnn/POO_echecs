# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:22:46 2026

@author: valer
"""

from Piece import Piece

class Pion(Piece):
    
    #Attributs spécifique au Pion
    a_deja_bouger: bool
    
    
    def __init__(self, couleur: str, position: "Case"= None):
        #On appelle le constructeur de Piece (super)
        super().__init__(couleur, position)
        
        #On initialise l'attribut spécifique
        self.a_deja_bouger = False
        
        
    def se_Deplacer(self, case_cible: "Case") -> bool:
        """
        Vérifie si le pion peut se déplacer.

        Parameters
        ----------
        case_cible : Case
            Correspond à la case que le joueur a cliqué.

        Returns
        -------
        bool
            Est-ce que le pion peut se déplacer ?
        """
        #la pièce connaît déjà sa position actuelle (self.position)
        depart = self.position
        #Les blancs montent (vers le haut, donc -1) et les noirs descendent (vers le bas, donc +1)
        direction = -1 if self.couleur == "blanc" else 1
        
        #calcul de la distance
        diff_ligne = case_cible.ligne - depart.ligne
        diff_colonne = case_cible.colonne - depart.colonne
        
        #1.Déplacement tout droit (on ne peut prednre une pièce adversaire qu'en avançant d'une case en diagonale)
        if diff_colonne == 0:
        #Avance d'une case (seulement si la case est vide)
            if diff_ligne == direction and case_cible.est_vide() == True :
                return True
        
        # Avance de deux cases (seulement si la case est vide et que le pion n'a pas bougé)
            if diff_ligne == 2 * direction and self.a_deja_bouger == False and case_cible.est_vide() == True:
                return True
            
            
        #2.Déplacement en diagonale pour prendre une pièce adverse
        elif abs(diff_colonne) == 1:
            if diff_ligne == direction:
                # On vérifie qu'il y a bien une pièce adverse à manger
                if case_cible.piece is not None and case_cible.piece.couleur != self.couleur:
                    return True
                
                
        # Si aucune condition n'est remplie, le déplacement est invalide
        return False
                
            