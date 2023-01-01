from question4 import *
import unittest


# calcul_detail(initialize("110_10", "multiplication.txt"))

class TestMachine(unittest.TestCase):
    def test_question_7(self):
        a = calcul_detail(initialize("110_10", "multiplication.txt"))
        self.assertTrue(a)

if __name__== "__main__":
    unittest.main()