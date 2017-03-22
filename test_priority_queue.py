import unittest
import binary_heap as bh
import priority_queue as pq


class TestPriorityQueue(unittest.TestCase):

    def test_heap_extract_max(self):
        a = bh.Array([3, 16, 7, 6])
        bh.build_max_heap(a)

        max_value = pq.heap_extract_max(a)

        self.assertEqual(max_value, 16)
        self.assertEqual(a, [7, 6, 3])
        
    def test_heap_increase_key(self):
        a = bh.Array([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
        bh.build_max_heap(a)

        pq.heap_increase_key(a, 8, 15)
        b = bh.Array([16, 15, 10, 14, 7, 9, 3, 2, 8, 1])

        self.assertEqual(a, b)

    def test_max_heap_insert(self):
        a = bh.Array([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
        bh.build_max_heap(a)

        pq.max_heap_insert(a, 20)
        b = bh.Array([20, 16, 10, 8, 14, 9, 3, 2, 4, 1, 7])

        self.assertEqual(a, b)



if __name__ == '__main__':
    unittest.main()

