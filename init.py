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
            elif self.pos_lecture[i] == -1:
                self.etat_bande[i].insert(0,"_")


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
            self.pos_lecture.append(0)
            if self.nb_bande > 1: # Si on utilise au moins 2 rubans
                for _ in range(self.nb_bande - 1):
                    self.etat_bande.append(["_" for _ in range(len(list(mot)))])
                    self.pos_lecture.append(0)

    
    def __str__(self):
        return "Rubans: {}\nNombre de ruban utilisé: {}\nliste des transitions: {}".format(self.etat_bande, self.nb_bande, self.transition)

    curseur_list = []
    def affiche(self):
        """
        affiche une etape de la machine
        Il faut 3 espaces pour atteindre la premiere pos, chaque pos est espacé de 5 espaces.
        """
        curseur = "↑"
        espace_depart = "   " # 3 espaces
        espace = "     "
        pos = 1

        print("--------------------------------------------------------")
        print(self.etat_bande)
        if self.tran_courant == None:
            self.curseur_list.append(espace_depart+curseur)
            print(self.curseur_list[0])
            for i in range(self.nb_bande - 1):
                self.curseur_list.append(espace*len(self.etat_bande[i])+espace+curseur)
                print(self.curseur_list[i+1])

        if type(self.tran_courant) == list:
            for i in range(self.nb_bande):
                if self.tran_courant[self.nb_bande+pos] == ">":
                    self.curseur_list[i] = espace+self.curseur_list[i]
                    print(self.curseur_list[i])
                if self.tran_courant[self.nb_bande+pos] == "<":
                    self.curseur_list[i] = self.curseur_list[i][5:]
                    print(self.curseur_list[i])
                if self.tran_courant[self.nb_bande+pos] == "-":
                    print(self.curseur_list[i])
                pos += 1
        print("--------------------------------------------------------")


def initialize(mot, path):
    mt = TM()
    mt.entree(mot, path)
    return mt

# print(initialize("0011", "data3.txt"))