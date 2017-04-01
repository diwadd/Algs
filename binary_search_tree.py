class Node:

    def __init__(self,
                 key = None,
                 p = None,                
                 left = None,
                 right = None,
                 data = None):
                 
        self.p = p
        self.left = left
        self.right = right
        self.key = key
        self.data = data

    def __str__(self):
    
        nk = "Node key: " + str(self.key) + "\n"
        np = "Node parrent: " + str(self.p) + "\n"
        nl = "Left child: " + str(self.left) + "\n"
        nr = "Right child: " + str(self.right) + "\n"
        
        return nk + np + nl + nr 
        
class BinarySearchTree:

    def __init__(self):
        self.root = None

        
    def tree_insert(self, node):
        """
        Insert a new node into the tree.
        """
    
        y = None
        x = self.root
        
        while x != None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.p = y

        if y == None:
            self.root = node
 
        elif node.key < y.key:
            y.left = node
        
        else:
            y.right = node


    def tree_minimum(self, x):

        while x.left != None:
            x = x.left
        return x


    def tree_maximum(self, x):

        while x.right != None:
            x = x.right
        return x


    def inorder_tree_walk(self, x):

        if (x != None):
            self.inorder_tree_walk(x.left)
            print(str(x.key) + " ")
            self.inorder_tree_walk(x.right)


if __name__ == '__main__':

    n = Node()
    print(n)
