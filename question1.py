import unittest

class TM:

    def __init__(self):
        self.etat_courant = "I"
        self.nb_bande = 0
        self.etat_bande = list()
        self.pos_lecture = list()
        self.transition = list()
        self.tran_courant = None


    def add_space(self):
        "Méthode qui permet d'ajouter des espaces si on veut lire au de-là de la taille du mot"
        for i in range(self.nb_bande):
            if self.pos_lecture[i] > len(self.etat_bande[i])-1:
                self.etat_bande[i].append("_")


    def entree(self, mot, path):
        "init la machine à partir d'un fichier"
        nb_ligne = 1
        with open(path, "r") as file:
            for line in file:
                if nb_ligne > 3:
                    if line == "\n":
                        continue
                    elif "\n" in line:
                        self.transition.append(line[0:len(line)-1])
                    else:
                        self.transition.append(line)
                nb_ligne += 1
            self.nb_bande = len(self.transition[0].split(","))-1
            self.etat_bande.append(list(mot)) # ajout du mot dans le premier ruban
            for _ in range(2):
                self.etat_bande[0].insert(0,"_") # ajout des espaces au début des bandes, peut être changer
            self.pos_lecture.append(2)
            if self.nb_bande > 1: # Si on utilise au moins 2 rubans
                for _ in range(self.nb_bande - 1):
                    self.etat_bande.append(["_" for _ in range(6)])
                    self.pos_lecture.append(2)


    def __str__(self):
        return "Rubans: {}".format(self.etat_bande)

    # curseur_list = []
    def affiche(self):
        """ Méthode pour plus de détails lors des pas"""

        print("--------------------------------------------------------")
        print(self.etat_bande)
        for i in range(self.nb_bande):
            if i+1 == self.nb_bande:
                print("Position de lecture du Ruban {} : {}".format(i+1,self.pos_lecture[i]))
            else:
                print("Position de lecture du Ruban {} : {}".format(i+1,self.pos_lecture[i]))
        print("--------------------------------------------------------")




        # curseur = "↑"
        # espace_depart = "   " # 3 espaces
        # espace = "     "
        # pos = 1

        # print("--------------------------------------------------------")
        # print(self.etat_bande)
        # if self.tran_courant == None:
        #     self.curseur_list.append(espace_depart+curseur)
        #     print(self.curseur_list[0])
        #     for i in range(self.nb_bande - 1):
        #         self.curseur_list.append(espace*len(self.etat_bande[i])+espace+curseur)
        #         print(self.curseur_list[i+1])

        # if type(self.tran_courant) == list:
        #     for i in range(self.nb_bande):
        #         if self.tran_courant[self.nb_bande+pos] == ">":
        #             self.curseur_list[i] = espace+self.curseur_list[i]
        #             print(self.curseur_list[i])
        #         if self.tran_courant[self.nb_bande+pos] == "<":
        #             self.curseur_list[i] = self.curseur_list[i][5:]
        #             print(self.curseur_list[i])
        #         if self.tran_courant[self.nb_bande+pos] == "-":
        #             print(self.curseur_list[i])
        #         pos += 1
        # print("--------------------------------------------------------")

    





def initialize(mot, path):
    mt = TM()
    mt.entree(mot, path)
    return mt

class TestMachine(unittest.TestCase):
    """On vérifie qu'il n'y a pas de transition doublon et pas d'espace dans le code de machine turing"""

    def test_doublon_transition(self):
        transition = []
        mt_doublon = []
        a = initialize("1100", "data.txt")
        
        for i in range(len(a.transition)):
            if i % 2 == 0:
                transition.append(a.transition[i])

        for i in range(len(transition)):
            if transition[i] not in mt_doublon:
                mt_doublon.append(transition[i])

        self.assertListEqual(transition, mt_doublon)

    def test_espace_transition(self):
        a = initialize("1100", "data.txt")
        b = "_"
        self.assertNotIn(b,a.transition)



if __name__== "__main__":
    print(initialize("0011", "data.txt"))
    unittest.main()