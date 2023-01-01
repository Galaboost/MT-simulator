from question1 import *
from question2 import *
import unittest


def calcul_detail(mt):
    etape = 1
    while mt.etat_courant != "F":
        print("Etape :", etape)
        etape += 1
        mt.affiche()
        step(mt)
    if mt.etat_courant == "F":
        print("Etape :", etape)
        mt.affiche()
        step(mt)
        print("Accepted")
    return True

calcul_detail(initialize("1001", "data.txt"))