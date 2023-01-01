from question1 import *


def calcul_step(mt):
    '''Pour traiter les differentes transitions, par rapport au nombre de bande, les symboles de transition 
    se trouve à nombre_bande + 1 et mettre à jour l'affichage pour la question 5'''
    pos = 1
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
        l.append(mt.etat_bande[i+1][mt.pos_lecture[i+1]])
    etat = ''.join(l)
    if etat in mt.transition:
        pos_etat = mt.transition.index(etat) # postion de l'etat où on se situe dans la liste des transitions
        mt.tran_courant = mt.transition[pos_etat+1].split(",") # la transition qu'on a besoin
        calcul_step(mt)
    

step(initialize("1001", "data.txt"))