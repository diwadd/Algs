import math
import binary_heap as bh


def heap_maximum(a):
    return a[0]


def heap_extract_max(a):
    """
    Intorduction to algorithms 3rd ed.
    Cormen et al.
    Page 163, Section 6.5

    Removes and returns the largest element.

    :param a: An array.

    """

    if a.heap_size < 1:
        return ValueError

    max_value = a[0]
    a[0] = a[a.heap_size - 1]
    a.pop()    

    a.heap_size = a.heap_size - 1

    bh.max_heapify(a, 0)

    return max_value


def heap_increase_key(a, i, key):
    """
    Intorduction to algorithms 3rd ed.
    Cormen et al.
    Page 164, Section 6.5

    Increases the value of element a[i] to key.
    Condition: key >= a[i].

    :param a: An array.
    :param i: Index in a.
    :param key: New value for a[i].
    """


    if key < a[i]:
        raise ValueError

    a[i] = key
    while i > 0 and a[bh.parent(i)] < a[i]:
        a[i], a[bh.parent(i)] = a[bh.parent(i)], a[i]
        i = bh.parent(i)


def max_heap_insert(a, key):
    """
    Intorduction to algorithms 3rd ed.
    Cormen et al.
    Page 164, Section 6.5

    Insert a new element into the heap.

    :param a: An array.
    :param key: New element to be inserted into the heap.
    """

    a.heap_size = a.heap_size + 1
    a.append(-math.inf)
    heap_increase_key(a, a.heap_size - 1, key)

    











