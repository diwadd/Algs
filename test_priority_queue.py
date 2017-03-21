import unittest
import binary_heap as bh
import priority_queue as pq


class TestPriorityQueue(unittest.TestCase):

    def test_heap_extract_max(self):
        a = bh.Array([2, 3, 10, 4, 16, 10, 11])
        bh.build_max_heap(a)

        max_value = pq.heap_extract_max(a)

        self.assertEqual(max_value, 16)


if __name__ == '__main__':
    unittest.main()

