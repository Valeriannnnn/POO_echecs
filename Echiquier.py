# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:27:29 2026

@author: valer
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:26:27 2026

@author: valer
"""

from Case import Case
from Tour import Tour
from Cavalier import Cavalier
from Fou import Fou
from Dame import Dame
from Roi import Roi
from Pion import Pion

import numpy as np

class Echiquier:
    
    #Attributs
    cases: np.ndarray
    case_en_passant: "Case"
    
    def __init__(self):
        #On crée la grille 8*8
        #dtype=object est indispensable pour stocker des objets, et pas juste des nombres
        self.cases = np.empty((8, 8), dtype=object)
        
        #on remplit la grille des objets case
        for c in range(8):
            for l in range(8):
                self.cases[l,c] = Case(l,c)
                
        self.case_en_passant = None
        
        # 3. On place les pièces au démarrage
        self.initialiser_plateau()
       
    def initialiser_plateau(self) -> None:
        """
        On place les pièces sur leur position de départ sur l'échiquier.

        Returns
        -------
        None
        """
           
        #Les pièces noires
        self.cases[0,0].piece = Tour("noir", "Tour_noir.png", self.cases[0,0])
        self.cases[0,1].piece = Cavalier("noir", "Cavalier_noir.png", self.cases[0,1])
        self.cases[0,2].piece = Fou("noir", "Fou_noir.png", self.cases[0,2])
        self.cases[0,3].piece = Dame("noir", "Dame_noir.png", self.cases[0,3])
        self.cases[0,4].piece = Roi("noir", "Roi_noir.png", self.cases[0,4])
        self.cases[0,5].piece = Fou("noir", "Fou_noir.png", self.cases[0,5])
        self.cases[0,6].piece = Cavalier("noir", "Cavalier_noir.png", self.cases[0,6])
        self.cases[0,7].piece = Tour("noir", "Tour_noir.png", self.cases[0,7])
        
        for c in range(8):
            self.cases[1,c].piece = Pion("noir", "Pion_noir.png", self.cases[1,c])


        #les pièces blanches
        self.cases[7,0].piece = Tour("blanc", "Tour_blanc.png", self.cases[7,0])
        self.cases[7,1].piece = Cavalier("blanc", "Cavalier_blanc.png", self.cases[7,1])
        self.cases[7,2].piece = Fou("blanc", "Fou_blanc.png", self.cases[7,2])
        self.cases[7,3].piece = Dame("blanc", "Dame_blanc.png", self.cases[7,3])
        self.cases[7,4].piece = Roi("blanc", "Roi_blanc.png", self.cases[7,4])
        self.cases[7,5].piece = Fou("blanc", "Fou_blanc.png", self.cases[7,5])
        self.cases[7,6].piece = Cavalier("blanc", "Cavalier_blanc.png", self.cases[7,6])
        self.cases[7,7].piece = Tour("blanc", "Tour_blanc.png", self.cases[7,7])
        
        for c in range(8):
            self.cases[6,c].piece = Pion("blanc", "Pion_blanc.png", self.cases[6,c])

    def deplacer_piece(self, depart: Case, arrivee: Case) -> bool:
        """
        Permet de déplacer une pièce.

        Parameters
        ----------
        depart : Case
            La case où se trouve la pièce.
        arrivee : Case
            La case où le joueur veut aller.

        Returns
        -------
        bool: True si le déplacement a réussi, False sinon.
        """
        #Vérifier que la case de départ n'est pas vide
        
        if depart.est_vide() == True:
            return False
                
        piece_depart = depart.piece
        piece_arrivee = arrivee.piece
        
        #Vérifier que la piece d'arrivee n'est pas de la même couleur car on ne peut pas prendre une pièce de notre propre couleur
        if piece_arrivee is not None and piece_arrivee.couleur == piece_depart.couleur:
            return False
        
        #Vérifier si la géométrie du déplacement de la pièce est autorisé
        if piece_depart.se_Deplacer(arrivee) == False:
            return False
            
        #Les conditions sont passées, on peut effectuer le déplacement
        arrivee.piece = depart.piece
        depart.piece = None
        piece_depart.position = arrivee
        
        # Si la pièce a un attribut a_deja_bouger (Pion, Roi, Tour), on le passe à True
        if hasattr(piece_depart, 'a_deja_bouger'):
           piece_depart.a_deja_bouger = True
        
        return True
    
    def afficher_plateau(self) -> None:
        """Affiche l'échiquier dans la console."""
        lettres = {
            "Pion": "P", "Tour": "T", "Cavalier": "C", 
            "Fou": "F", "Dame": "D", "Roi": "R"
        }
        
        print("\n  a b c d e f g h")
        for ligne in range(8):
            print(f"{8 - ligne} ", end="")
            
            for colonne in range(8):
                piece = self.cases[ligne, colonne].piece
                
                if piece is None:
                    print(".", end=" ")
                else:
                    # Tout ce qui suit doit être DANS le else !
                    nom_classe = piece.__class__.__name__
                    lettre = lettres.get(nom_classe, "?")
                    
                    if piece.couleur == "noir":
                        lettre = lettre.lower()
                        
                    print(lettre, end=" ")
                    
            print() # Retour à la ligne
        print()