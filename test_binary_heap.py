import unittest
import ads.binary_heap as bh

class TestBinaryHeap(unittest.TestCase):

    def test_max_heapify(self):
        a = bh.Array([16, 4, 10, 14, 7, 9, 3, 2, 8, 1])
        b = bh.Array([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()


