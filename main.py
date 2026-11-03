from Partie import Partie
from Joueur import Joueur

if __name__ == "__main__":
    #On crée les deux joueurs
    alice = Joueur("Alice", "blanc")
    bob = Joueur("Bob", "noir")
    
    #On initialise la partie avec ces deux joueurs
    ma_partie = Partie(alice, bob)
    
    #On lance le jeu.
    ma_partie.demarrer()