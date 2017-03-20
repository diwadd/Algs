import binary_heap as bh

a = [0, 16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

print("Testing the heap")
print(a)
bh.max_heapify(a, 2)

print(a)
bh.max_heapify(a, 3)

print(a)