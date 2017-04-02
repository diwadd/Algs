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


    def test_inorder_tree_walk(self):

        t = BinarySearchTree()

        t.tree_insert(Node(key=6))
        t.tree_insert(Node(key=5))
        t.tree_insert(Node(key=7))
        t.tree_insert(Node(key=2))
        t.tree_insert(Node(key=5))
        t.tree_insert(Node(key=8))

        walk = t.inorder_tree_walk(t.root)
        
        self.assertTrue(walk, [2, 5, 5, 6, 7, 8])

    def test_tree_search(self):

        t = BinarySearchTree()

        t.tree_insert(Node(key=16, data="a"))
        t.tree_insert(Node(key=52, data="b"))
        t.tree_insert(Node(key=73, data="c"))
        t.tree_insert(Node(key=12, data="d"))
        t.tree_insert(Node(key= 5, data="e"))
        t.tree_insert(Node(key=98, data="f"))

        found_node = t.tree_search(t.root, 12)
        
        self.assertEqual(found_node.key, 12)
        self.assertEqual(found_node.data, "d")


    def test_iterative_tree_search(self):

        t = BinarySearchTree()

        t.tree_insert(Node(key=67, data="x"))
        t.tree_insert(Node(key=23, data="y"))
        t.tree_insert(Node(key=37, data="z"))
        t.tree_insert(Node(key=-5, data="w"))
        t.tree_insert(Node(key=68, data="a"))

        found_node = t.iterative_tree_search(t.root, 23)
        
        self.assertEqual(found_node.key, 23)
        self.assertEqual(found_node.data, "y")


if __name__ == '__main__':
    unittest.main()

