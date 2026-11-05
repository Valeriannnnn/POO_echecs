# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:27:29 2026

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
        
        # On place les pièces au démarrage
        self.initialiser_plateau()

       
    def initialiser_plateau(self) -> None:
        """
        On place les pièces sur leur position de départ sur l'échiquier.

        Returns
        -------
        None
        """
           
        #Les pièces noires
        self.cases[0,0].piece = Tour("noir", self.cases[0,0])
        self.cases[0,1].piece = Cavalier("noir", self.cases[0,1])
        self.cases[0,2].piece = Fou("noir", self.cases[0,2])
        self.cases[0,3].piece = Dame("noir", self.cases[0,3])
        self.cases[0,4].piece = Roi("noir", self.cases[0,4])
        self.cases[0,5].piece = Fou("noir", self.cases[0,5])
        self.cases[0,6].piece = Cavalier("noir", self.cases[0,6])
        self.cases[0,7].piece = Tour("noir", self.cases[0,7])
        
        for c in range(8):
            self.cases[1,c].piece = Pion("noir", self.cases[1,c])


        #les pièces blanches
        self.cases[7,0].piece = Tour("blanc", self.cases[7,0])
        self.cases[7,1].piece = Cavalier("blanc", self.cases[7,1])
        self.cases[7,2].piece = Fou("blanc", self.cases[7,2])
        self.cases[7,3].piece = Dame("blanc", self.cases[7,3])
        self.cases[7,4].piece = Roi("blanc", self.cases[7,4])
        self.cases[7,5].piece = Fou("blanc", self.cases[7,5])
        self.cases[7,6].piece = Cavalier("blanc", self.cases[7,6])
        self.cases[7,7].piece = Tour("blanc", self.cases[7,7])
        
        for c in range(8):
            self.cases[6,c].piece = Pion("blanc", self.cases[6,c])


    def deplacer_piece(self, depart: Case, arrivee: Case) -> bool:
        # 1. Vérifier que la case de départ n'est pas vide
        if depart.est_vide():
            return False
                
        piece_depart = depart.piece
        piece_arrivee = arrivee.piece
        
        # 2. Vérifier qu'on ne mange pas sa propre pièce
        if piece_arrivee is not None and piece_arrivee.couleur == piece_depart.couleur:
            return False
            
        # 3. --- DÉTECTION DU ROQUE ---
        if piece_depart.__class__.__name__ == "Roi" and abs(arrivee.colonne - depart.colonne) == 2:
            if arrivee.colonne > depart.colonne:
                return self.effectuer_petit_roque(piece_depart.couleur)
            else:
                return self.effectuer_grand_roque(piece_depart.couleur)
            
        # 4. Vérifier la géométrie de la pièce
        if not piece_depart.se_Deplacer(arrivee):
            return False
            
        # 5. Vérifier les collisions
        if piece_depart.__class__.__name__ != "Cavalier":
            if not self.chemin_est_libre(depart, arrivee):
                return False
        
        
        # 6. Simuler le déplacement pour vérifier si le Roi est en échec après le coup
        # On sauvegarde l'état de la case d'arrivée (au cas où on capture)
        piece_mangee = arrivee.piece
        
        # On simule le déplacement
        arrivee.piece = piece_depart
        depart.piece = None
        
        # On vérifie si notre Roi est en échec après ce mouvement
        est_illegal = self.est_en_echec(piece_depart.couleur)
        
        # On annule le déplacement (retour en arrière)
        depart.piece = piece_depart
        arrivee.piece = piece_mangee
        
        if est_illegal:
            return False # Le coup est refusé
        
            
        # 7. Les conditions sont TOUTES passées, on effectue le vrai déplacement
        arrivee.piece = piece_depart
        depart.piece = None
        piece_depart.position = arrivee
        
        # 8. Vérification de la promotion
        self.promouvoir_pion(arrivee)
        
        # 9. Mise à jour de a_deja_bouger
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


    def chemin_est_libre(self, depart: Case, arrivee: Case) -> bool:
        """
        Vérifie qu'il n'y a pas de pièce sur le chemin entre le départ et l'arrivée.
        """
        # On calcule le sens du déplacement (1 si on avance, -1 si on recule, 0 si on reste sur la ligne/colonne)
        pas_ligne = (arrivee.ligne > depart.ligne) - (arrivee.ligne < depart.ligne)
        pas_colonne = (arrivee.colonne > depart.colonne) - (arrivee.colonne < depart.colonne)
        
        # On se place sur la toute première case après le départ
        ligne_actuelle = depart.ligne + pas_ligne
        colonne_actuelle = depart.colonne + pas_colonne
        
        # On avance case par case jusqu'à arriver juste avant la destination
        while (ligne_actuelle != arrivee.ligne) or (colonne_actuelle != arrivee.colonne):
            # Si on trouve une pièce sur notre route, le chemin est bloqué
            if not self.cases[ligne_actuelle, colonne_actuelle].est_vide():
                return False 
            
            # Sinon, on avance d'une case dans la même direction
            ligne_actuelle += pas_ligne
            colonne_actuelle += pas_colonne
            
        return True


    def effectuer_petit_roque(self, couleur: str) -> bool:
        """Gère le petit roque (côté Roi)."""
        ligne = 7 if couleur == "blanc" else 0
        roi = self.cases[ligne, 4].piece
        tour = self.cases[ligne, 7].piece

        # Vérifications de base (les pièces sont-elles là ? ont-elles bougé ?)
        if roi is None or tour is None: return False
        if roi.a_deja_bouger or tour.a_deja_bouger: return False

        # Vérifier que le chemin est libre (entre la colonne 4 et 7)
        if not self.chemin_est_libre(self.cases[ligne, 4], self.cases[ligne, 7]):
            return False

        # Déplacement du Roi (de e1 à g1)
        self.cases[ligne, 6].piece = roi
        self.cases[ligne, 4].piece = None
        roi.position = self.cases[ligne, 6]
        roi.a_deja_bouger = True

        # Déplacement de la Tour (de h1 à f1)
        self.cases[ligne, 5].piece = tour
        self.cases[ligne, 7].piece = None
        tour.position = self.cases[ligne, 5]
        tour.a_deja_bouger = True

        return True


    def effectuer_grand_roque(self, couleur: str) -> bool:
        """Gère le grand roque (côté Dame)."""
        ligne = 7 if couleur == "blanc" else 0
        roi = self.cases[ligne, 4].piece
        tour = self.cases[ligne, 0].piece

        # Vérifications de base
        if roi is None or tour is None: return False
        if roi.a_deja_bouger or tour.a_deja_bouger: return False

        # érifier que le chemin est libre (entre la colonne 4 et 0)
        if not self.chemin_est_libre(self.cases[ligne, 4], self.cases[ligne, 0]):
            return False

        # Déplacement du Roi (de e1 à c1)
        self.cases[ligne, 2].piece = roi
        self.cases[ligne, 4].piece = None
        roi.position = self.cases[ligne, 2]
        roi.a_deja_bouger = True

        # Déplacement de la Tour (de a1 à d1)
        self.cases[ligne, 3].piece = tour
        self.cases[ligne, 0].piece = None
        tour.position = self.cases[ligne, 3]
        tour.a_deja_bouger = True

        return True

    def promouvoir_pion(self, case: Case) -> bool:
        """
        Transforme un pion arrivé au bout du plateau en Dame.
        Retourne True si une promotion a eu lieu, False sinon.
        """
        piece = case.piece
        
        # On vérifie que c'est bien un pion
        if piece is None or piece.__class__.__name__ != "Pion":
            return False
            
        ligne_promotion = 0 if piece.couleur == "blanc" else 7
        
        # On vérifie que le pion est sur la dernière ligne
        if case.ligne == ligne_promotion:
            # On remplace le pion par une Dame de la même couleur
            case.piece = Dame(piece.couleur, case)
            return True
            
        return False

    def est_en_echec(self, couleur: str) -> bool:
        """
        Vérifie si le Roi de la couleur donnée est actuellement attaqué.
        """
        # Trouver la case du Roi
        case_roi = None
        for ligne in range(8):
            for colonne in range(8):
                piece = self.cases[ligne, colonne].piece
                if (piece is not None and 
                    piece.__class__.__name__ == "Roi" and 
                    piece.couleur == couleur):
                    case_roi = self.cases[ligne, colonne]
                    break
            if case_roi is not None:
                break
                
        if case_roi is None:
            return False # Sécurité (au cas où le Roi n'est pas sur le plateau)

        # Regarder toutes les pièces adverses
        couleur_adverse = "noir" if couleur == "blanc" else "blanc"
        
        for ligne in range(8):
            for colonne in range(8):
                piece = self.cases[ligne, colonne].piece
                
                # Si c'est une pièce adverse
                if piece is not None and piece.couleur == couleur_adverse:
                    
                    # Est-ce que sa géométrie lui permet d'atteindre le Roi ?
                    if piece.se_Deplacer(case_roi):
                        
                        # Est-ce que le chemin est libre ? (sauf pour le Cavalier)
                        if piece.__class__.__name__ == "Cavalier":
                            return True
                        elif self.chemin_est_libre(self.cases[ligne, colonne], case_roi):
                            return True
                            
        return False

    def a_des_coups_legaux(self, couleur: str) -> bool:
        """
        Vérifie si le joueur a au moins un coup légal possible.
        """
        for ligne in range(8):
            for colonne in range(8):
                piece = self.cases[ligne, colonne].piece
                
                if piece is not None and piece.couleur == couleur:
                    for l_dest in range(8):
                        for c_dest in range(8):
                            depart = self.cases[ligne, colonne]
                            arrivee = self.cases[l_dest, c_dest]
                            
                            # On teste le déplacement (qui gère déjà l'échec)
                            if self.deplacer_piece(depart, arrivee):
                                
                                # Si le coup est valide, on annule le déplacement 
                                # pour ne pas modifier le vrai plateau pendant la simulation.
                                piece_mangee = arrivee.piece
                                arrivee.piece = depart.piece
                                depart.piece = piece_mangee
                                
                                if piece_mangee is not None:
                                    piece_mangee.position = arrivee
                                piece.position = depart
                                
                                return True # Un coup valide existe, le roi peut être sauvé
        return False

    def est_echec_et_mat(self, couleur: str) -> bool:
        """
        Vérifie si le joueur est échec et mat (en échec ET aucun coup légal).
        """
        # Si le Roi n'est pas en échec, ce n'est pas un mat
        if not self.est_en_echec(couleur):
            return False
            
        # Si le Roi est en échec, on regarde s'il a un moyen de s'en sortir
        return not self.a_des_coups_legaux(couleur)