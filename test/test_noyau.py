from noyau import *
import pytest

    # Test en condition normale
def test_noyau_jeton():
    grille = ((6, 7), -1)
    joueur = 0
    posx = 7
    posy = 6
    depx = 1
    depy = 0
    expected = 0
    assert expected == jeton(joueur, posx, posy, depx, depy, grille)

    # Jeton hors limites 
    grille = ((6, 7), -1)
    joueur = 0
    posx = 6
    posy = 7
    depx = 1
    depy = 0
    expected = 0
    assert expected == jeton(joueur, posx, posy, depx, depy, grille)


def test_changerjoueur():
    assert (changer_joueur(1)) == 0
    assert (changer_joueur(2)) == 1
    assert (changer_joueur(43)) == None

def test_coup_gagnant():
    grille = [
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 0, -1, -1, -1]
    ]
    assert not coup_gagnant(0, 2, 3, grille)
    grille_vertical = [
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [0, -1, -1, -1, -1, -1, -1],
        [0, -1, -1, -1, -1, -1, -1],
        [0, -1, -1, -1, -1, -1, -1],
        [0, -1, -1, -1, -1, -1, -1]
    ]
    assert coup_gagnant(0, 2, 0, grille_vertical)
    grille_horizontal = [
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [0, 0, 0, 0, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1]
    ]
    assert coup_gagnant(0, 3, 3, grille_horizontal)
    grille_diagonaled = [
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 1, -1, -1, -1],
        [-1, -1, 1, -1, -1, -1, -1],
        [-1, 1, -1, -1, -1, -1, -1],
        [1, -1, -1, -1, -1, -1, -1]
    ]
    assert coup_gagnant(1, 2, 3, grille_diagonaled)
    grille_diagonaleg = [
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, 1, -1, -1, -1, -1],
        [-1, -1, -1, 1, -1, -1, -1],
        [-1, -1, -1, -1, 1, -1, -1],
        [-1, -1, -1, -1, -1, 1, -1]
    ]
    assert coup_gagnant(1, 2, 2, grille_diagonaleg)

def test_maj_jeu():
    grille_initiale = [
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1]
    ]
    assert maj_jeu((0,2), grille_initiale, [5,5,5,5,5,5,5], 0) == (5,2)

    grille_partielle = [
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [0, -1, -1, -1, -1, -1, -1],
        [1, -1, -1, -1, -1, -1, -1],
        [0, -1, -1, -1, -1, -1, -1] 
    ]
    assert maj_jeu((0,0), grille_partielle, [2,5,5,5,5,5,5], 1) == (2,0)

    grille_pleine = [
        [1, -1, -1, -1, -1, -1, -1],
        [0, -1, -1, -1, -1, -1, -1],
        [1, -1, -1, -1, -1, -1, -1],
        [0, -1, -1, -1, -1, -1, -1],
        [1, -1, -1, -1, -1, -1, -1],
        [0, -1, -1, -1, -1, -1, -1]     
    ]
    assert maj_jeu((0,0), grille_pleine, [0,5,5,5,5,5,5], 0) == (None, None)


