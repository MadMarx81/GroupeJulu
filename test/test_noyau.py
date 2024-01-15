from noyau import *

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


