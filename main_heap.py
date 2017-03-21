import binary_heap as bh



a = bh.Array([16, 4, 10, 14, 7, 9, 3, 2, 8, 1])

print("Testing the heap")
print(a)
bh.max_heapify(a, 1)

#print(a)
#bh.max_heapify(a, 3)

print(a)


print("Building a heap")

b = bh.Array([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
print(b)

bh.build_max_heap(b)
print(b)


c = bh.Array([5,4,2,7,4,37,8,7])
print(c)
bh.heapsort(c)
print(c)



h = bh.Array([1,2,3,4,5,6])
print(h)
print(h.heap_size)
