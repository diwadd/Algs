import unittest
import binary_heap as bh

class TestBinaryHeap(unittest.TestCase):

    def test_max_heapify(self):
        a = bh.Array([16, 4, 10, 14, 7, 9, 3, 2, 8, 1])
        bh.max_heapify(a, 1)

        b = bh.Array([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
        self.assertEqual(a , b)

    def test_build_max_heap(self):
        a = bh.Array([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
        bh.build_max_heap(a)

        b = bh.Array([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
        self.assertEqual(a , b)

    def test_heapsort(self):
        a = bh.Array([3, 2, 5, 6, 7, 2 ,1, 7])
        bh.heapsort(a)

        b = bh.Array([1, 2, 2, 3, 5, 6, 7, 7])
        self.assertEqual(a , b)


if __name__ == '__main__':
    unittest.main()


