import unittest
import quicksort as qs

class TestQuciksort(unittest.TestCase):

    def test_partition(self):
        a = [2, 1, 3]
        q = qs.partition(a, 0, len(a) - 1)

        self.assertEqual(q, 2)


    def test_quicksort(self):
        a = [4, 3, 2, 5, 6, 1]
        qs.quicksort(a, 0, len(a) - 1)

        b = [1, 2, 3, 4, 5, 6]
        self.assertEqual(a, b)


    def test_quicksort_negative_numbers(self):
        a = [-5, -2, -3, -1, -4, -6]
        qs.quicksort(a, 0, len(a) - 1)

        b = [-6, -5, -4, -3, -2, -1]
        self.assertEqual(a, b)


    def test_randomized_quicksort(self):
        a = [3, 2, 4, 1, 5, 6]
        qs.randomized_quicksort(a, 0, len(a) - 1)

        b = [1, 2, 3, 4, 5, 6]
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()
