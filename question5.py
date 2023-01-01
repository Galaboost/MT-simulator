from question4 import *


def left():
    print()
    print("Positionner la tête de lecture sur la lettre la plus à droite")
    print("--------------------------------------------------------")
    calcul_detail(initialize("1100", "left.txt"))

def search():
    print()
    print("Positionner la tête de lecture sur le premier caractère")
    print("--------------------------------------------------------")
    calcul_detail(initialize("0010", "search.txt"))

def erased():
    print()
    print("Effacer la bande")
    print("--------------------------------------------------------")
    calcul_detail(initialize("0010", "erased.txt"))

def copy():
    print()
    print("Copy bande")
    print("--------------------------------------------------------")
    calcul_detail(initialize("0010", "copy.txt"))

# left()
# search()
# erased()
# copy()