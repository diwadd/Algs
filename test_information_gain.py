import unittest
import numpy as np
import information_gain as ig

PRECISION = 14

FT1 = [[0, 1],
       [1, 1],
       [1, 1],
       [1, 0],
       [0, 0],
       [0, 0]]
FT1 = np.array(FT1)

FT2 = [[1, 1],
       [0, 1],
       [0, 1],
       [1, 0],
       [0, 0],
       [0, 0]]
FT2 = np.array(FT2)

FT3 = [[1, 1],
       [1, 1],
       [1, 1],
       [0, 0],
       [0, 0],
       [0, 0]]
FT3 = np.array(FT3)



class TestInformationGain(unittest.TestCase):

    def test_shannon_entropy(self):
        x = [0, 0, 0, 1, 1, 1]
        h = ig.shannon_entropy(x)

        entropy_ok = round(h, PRECISION) == round(1.0, PRECISION)
        self.assertTrue(entropy_ok)

        x = [0, 0, 0,
             0, 0, 0,
             0, 0, 0,
             1, 1, 1]
        h = ig.shannon_entropy(x)

        entropy_ok = round(h, PRECISION) == round(0.811278124459132, PRECISION)
        self.assertTrue(entropy_ok)

    def test_information_gain(self):

        i_gain = ig.information_gain(FT1)
        i_gain_ok = round(i_gain, PRECISION) == round(0.08170416594551044, PRECISION)
        self.assertTrue(i_gain_ok)


if __name__ == '__main__':
    unittest.main()
