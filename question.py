from init import *

# Question 2)

def calcul_step(mt):
    '''Pour traiter les differentes transitions, par rapport au nombre de bande, les symboles de transition 
    se trouve à nombre_bande + 1 et mettre à jour l'affichage pour la question 5'''
    pos = 1
    # print(mt.etat_bande)
    for i in range(mt.nb_bande):
        mt.etat_bande[i][mt.pos_lecture[i]] = mt.tran_courant[pos]
        if mt.tran_courant[mt.nb_bande+pos] == ">":
            mt.pos_lecture[i] += 1
            mt.etat_courant = mt.tran_courant[0]
        if mt.tran_courant[mt.nb_bande+pos] == "<":
            mt.pos_lecture[i] -= 1
            mt.etat_courant = mt.tran_courant[0]
        if mt.tran_courant[mt.nb_bande+pos] == "-":
            mt.pos_lecture[i] += 0
            mt.etat_courant = mt.tran_courant[0]
        pos += 1


def step(mt):
    mt.add_space()
    l = [mt.etat_courant,",", mt.etat_bande[0][mt.pos_lecture[0]]]
    for i in range(mt.nb_bande-1):
        l.append(",")
        l.append(mt.etat_bande[i+1][mt.pos_lecture[i]])
    etat = ''.join(l)
    if etat in mt.transition:
        # print(etat)
        pos_etat = mt.transition.index(etat) # postion de l'etat où on se situe dans la liste des transitions
        mt.tran_courant = mt.transition[pos_etat+1].split(",") # la transition qu'on a besoin
        # print(mt.tran_courant)
        calcul_step(mt)

# step(initialize("1001", "data2.txt"))

#--------------------------------------------------------------------------------------------------------

# Question 3)

def calcul(mt):
    while mt.etat_courant != "F":
        step(mt)
    print("Accepted")

# calcul(initialize("1100", "data.txt"))

#--------------------------------------------------------------------------------------------------------

# Question 4)

def calcul_detail(mt):
    etape = 1
    while mt.etat_courant != "F":
    # for _ in range(5):
        print("Etape :", etape)
        etape += 1
        mt.affiche()
        step(mt)
    if mt.etat_courant == "F":
        print("Etape :", etape)
        mt.affiche()
        step(mt)

# calcul_detail(initialize("1100", "data.txt"))

#--------------------------------------------------------------------------------------------------------

# Question 5)

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

#--------------------------------------------------------------------------------------------------------

# Question 6