import random

def partition(a, p, r):
    """
    Intorduction to algorithms 3rd ed.
    Cormen et al.
    Page 171, Section 7.1

    :param a: An array.
    :param p: Index in a.
    :param r: Index in a.
    """

    x = a[r]
    i = p - 1

    for j in range(p, r):
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
            
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def randomized_partition(a, p, r):
    """
    Intorduction to algorithms 3rd ed.
    Cormen et al.
    Page 179, Section 7.3

    :param a: An array.
    :param p: Index in a.
    :param r: Index in a.
    """    

    i = random.randint(p, r)
    a[i], a[r] = a[r], a[i]
    return partition(a, p, r)
    

def quicksort(a, p, r):
    """
    Intorduction to algorithms 3rd ed.
    Cormen et al.
    Page 171, Section 7.1

    :param a: An array.
    :param p: Index in a.
    :param r: Index in a.
    """

    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q + 1, r)


def randomized_quicksort(a, p, r):
    """
    Intorduction to algorithms 3rd ed.
    Cormen et al.
    Page 179, Section 7.3

    :param a: An array.
    :param p: Index in a.
    :param r: Index in a.
    """ 

    if p < r:
        q = randomized_partition(a, p, r)
        randomized_quicksort(a, p, q - 1)
        randomized_quicksort(a, q + 1, r)




