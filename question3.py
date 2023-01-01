from question2 import *
import unittest

def calcul(mt):
    while mt.etat_courant != "F":
        step(mt)
    print("Accepted")
    return True



class TestMachine(unittest.TestCase):

    def test_question_3(self):
        a = calcul(initialize("1100", "data.txt"))
        self.assertTrue(a)

if __name__== "__main__":
    unittest.main()