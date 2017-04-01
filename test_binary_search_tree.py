import unittest
from binary_search_tree import *

class TestPriorityQueue(unittest.TestCase):

    def test_tree_minimum(self):

        t = BinarySearchTree()

        t.tree_insert(Node(key=5))
        t.tree_insert(Node(key=6))
        t.tree_insert(Node(key=2))
        t.tree_insert(Node(key=3))
        t.tree_insert(Node(key=4))

        tm = t.tree_minimum(t.root)

        self.assertEqual(tm.key, 2)
        

    def test_tree_maximum(self):

        t = BinarySearchTree()

        t.tree_insert(Node(key=2))
        t.tree_insert(Node(key=0))
        t.tree_insert(Node(key=7))
        t.tree_insert(Node(key=9))
        t.tree_insert(Node(key=5))

        tm = t.tree_maximum(t.root)

        self.assertEqual(tm.key, 9)        

    """
    def test_inorder_tree_walk(self):

        t = BinarySearchTree()

        t.tree_insert(Node(key=6))
        t.tree_insert(Node(key=5))
        t.tree_insert(Node(key=7))
        t.tree_insert(Node(key=2))
        t.tree_insert(Node(key=5))
        t.tree_insert(Node(key=8))

        inorder_tree_walk_string = t.inorder_tree_walk(t.root)

        self.assertEqual(inorder_tree_walk_string,
                         "2 5 5 6 7 8 ")
    """



if __name__ == '__main__':
    unittest.main()

