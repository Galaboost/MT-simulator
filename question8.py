from question4 import *
import unittest



# print(calcul_detail(initialize("01#00#11#00#10", "tri.txt")))

class TestMachine(unittest.TestCase):
    def test_question_8(self):
        a = calcul_detail(initialize("01#00#11#00#10", "tri.txt"))
        self.assertTrue(a)

if __name__== "__main__":
    unittest.main()