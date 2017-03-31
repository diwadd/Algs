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
        self.root = Node()
        
    def tree_insert(self, node):
        """
        Insert a new node with value z into the tree.
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
 
if __name__ == '__main__':

    n = Node()
    print(n)
