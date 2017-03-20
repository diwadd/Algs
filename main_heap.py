import binary_heap as bh

a = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

print("Testing the heap")
print(a)
bh.max_heapify(a, 2)

#print(a)
#bh.max_heapify(a, 3)

print(a)


print("Building a heap")

b = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
print(b)

bh.build_max_heap(b)
print(b)
