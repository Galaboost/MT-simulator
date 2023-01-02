from question4 import *

new_transition = []

def new_step(mt):
    """Léger modif pour avoir que les transitions utilisé"""
    mt.add_space()
    l = [mt.etat_courant,",", mt.etat_bande[0][mt.pos_lecture[0]]]
    for i in range(mt.nb_bande-1):
        l.append(",")
        l.append(mt.etat_bande[i+1][mt.pos_lecture[i+1]])
    etat = ''.join(l)
    if etat in mt.transition:
        new_transition.append(etat)
        pos_etat = mt.transition.index(etat) # postion de l'etat où on se situe dans la liste des transitions
        mt.tran_courant = mt.transition[pos_etat+1].split(",") # la transition qu'on a besoin
        calcul_step(mt)

def useless_transition(mt):
    while mt.etat_courant != "F":
        new_step(mt)
    mt.transition = new_transition
    return mt

if __name__ == "__main__":
    a = useless_transition(initialize("1100", "data.txt"))
    print(a.transition)
