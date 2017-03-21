import math
import binary_heap as bh


def heap_maximum(a):
    return a[0]


def heap_extract_max(a):
    if a.heap_size < 1:
        return ValueError

    max_value = a[0]
    a[0] = a[a.heap_size - 1]
    a.pop()    

    a.heap_size = a.heap_size - 1

    bh.max_heapify(a, 0)

    return max_value
