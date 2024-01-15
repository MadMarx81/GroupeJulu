from noyau import *
def test_integration_jouer() :
    grille_initiale = [
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1]
    ]
    niveau_initial = [5, 5, 5, 5, 5, 5, 5]
    etat_initiale = "en cours"

    case = "03"
    gbouton = [[None]*7 for _ in range(6)] 
    message = {'config': lambda **kwargs: None}

    jouer(case, gbouton, message)

    assert etat_initiale == "fini"

    assert coup_gagnant(0, 0, 0, grille_initiale)

    assert grille_initiale == [
        [0, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1]
    ]
