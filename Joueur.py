# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 12:05:24 2026

@author: valer
"""

class Joueur:
    #Attributs
    name: str
    color: str
    piecesCapturees: list
    
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color
        self.piecesCapturees = []
        
    def jouer_un_coup(self):
        """
        Permet de déplacer une pièce. J'imagine que cette fonction va faire appel
        à la fonction "se_Déplacer" de piece
        
        Returns
        -------
        Bool: Est-ce que le déplacement est autorisé ?
        Case: Renvoie la case choisie
        """
        pass
        
    def abandonner_la_partie(self):
        """
        Permet de choisir d'abandonner une partie. Une fenêtre devra ainsi s'ouvrire,
        demandant si le joueur est sûr de lui. En fonction de son choix, il continuera
        ou perdra la partie.

        Returns
        -------
        Bool: Choisis-tu d'abandonner ?
        """
        pass
    
    def proposer_match_nul(self):
        """
        Permet de proposer au joueur en face de faire un match nul. Une fenêtre devra s'ouvrire
        pour le joueur en face afin de savoir s'il accepte ou pas.

        Returns
        -------
        Bool: Voulez-vous faire un match nul ?
        """
        pass
    
    