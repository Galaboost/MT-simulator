class TM:
# Proposer une structure de donnees MT (une class en Python) 
# qui permet de représenter une machine de Turing ainsi 
# que sa configuration (´etat courant, ´etat des bandes, position des 
# tetes de lecture). Ecrire une fonction qui initialise une 
# instance de la structure ´ MT `a partir d’un mot d’entree et d’un fichier
# contenant une description d’une machine de Turing.
    def __init__(self):
        self.etat_courant = "I"
        self.nb_bande = None
        self.etat_bande = list()
        self.pos_lecture = '_'
        self.transition = list()
    
    def entree(self, mot, path):
        "init la machine à partir d'un fichier"
        with open(path, "r") as file:
            nb_ligne = 1
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
            self.etat_bande.append(list(mot))
    
    def __str__(self):
        return "Rubans : {}, Nombre de ruban utilisé: {}".format(self.etat_bande, self.nb_bande)

if __name__ == "__main__":
    mt = TM()
    mt.entree("1011", "data.txt")
    print(mt.__str__())

