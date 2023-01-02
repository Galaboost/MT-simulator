from question4 import *
from question3 import *

test = []

def n_step(mt):
    pos = 1
    mt.add_space()
    l = [mt.etat_courant,",", mt.etat_bande[0][mt.pos_lecture[0]]]
    for i in range(mt.nb_bande-1):
        l.append(",")
        l.append(mt.etat_bande[i+1][mt.pos_lecture[i+1]])
    etat = ''.join(l)
    if etat in mt.transition:
        pos_etat = mt.transition.index(etat) # postion de l'etat où on se situe dans la liste des transitions
        mt.tran_courant = mt.transition[pos_etat+1].split(",") # la transition qu'on a besoin

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
        if mt.tran_courant[mt.nb_bande+pos] == "left.txt":
            test.append(mt.tran_courant[0])
            mt2 = linker("1001", "left.txt")
            calcul(mt2)
            mt.etat_courant = test[0]
            mt.pos_lecture = mt2.pos_lecture
        pos += 1


def new_calcul_detail(mt):
    etape = 1
    while mt.etat_courant != "F":
        print("Etape :", etape)
        etape += 1
        mt.affiche()
        n_step(mt)
    if mt.etat_courant == "F":
        mt = initialize("1001", "data2.txt")
        print("Etape :", etape)
        mt.affiche()
        n_step(mt)
        print("Accepted")

def linker(mot,path1):
    mt1 = initialize(mot,path1)
    return mt1


if __name__ == "__main__":
    new_calcul_detail(linker("1001", "data2.txt"))
