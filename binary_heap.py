import math

def parent(i):
    """
    Return parent of node i.
    For arrays indexed from 1 to N floor(i/2).
    :param i: node index
    :return: parent index
    """
    return math.floor((i - 1) / 2)

    
def left(i):
    """
    Return the left child of nod with index i.
    For arrays indexed from 1 to N 2 * i.
    """
    return 2 * i + 1
 
 
def right(i):
    """
    Return the right child of nod with index i.
    For arrays indexed from 1 to N 2 * i + 1.
    """
    return 2 * i + 2
    
def max_heapify(a, i):
    """"
    Intorduction to algorithms 3rd ed.
    Cormen et al.
    Page 154, Section 6.2
    
    :param a: An array
    :param i: Index in a.
    """
    le = left(i)
    ri = right(i)
    largest = None
    
    # Python lists are dynamic so a.heap-size = len(a)
    if le <= len(a) and a[le] > a[i]:
        largest = le
    else:
        largest = i
    if ri <= len(a) and a[ri] > a[largest]:
        largest = ri
    if largest != i:
        # exchange a[i] with a[largest]
        b = a[i]
        a[i] = a[largest]
        a[largest] = b
        max_heapify(a, largest)
    
    
    
    
    
    
    
    
    
    
