import math


def next_smallest_element_n2(a):

    n = len(a)
    for i in range(n):
        found = False
        for j in range(i,n):
            if(a[j] < a[i]):
                print(f"{a[i]} - {a[j]}")
                found = True
                break
        if found == False:
            print(f"{a[i]} - -1")

def next_smallest_element_fast(a):

    stack = []
    stack.append(a[0])
    n = len(a)
    for i in range(1, n):

        if(len(stack) == 0):
            stack.append(a[i])
            continue

        while (len(stack) != 0):
            if stack[-1] > a[i]:
                print(f"{stack.pop()} - {a[i]}")
            else:
                break

        stack.append(a[i])
    
    while (len(stack) != 0):
        print(f"{stack.pop()} - -1")



if __name__ == "__main__":
    
    a = [2,3,4,5,3,2,3,4,6,4]
    print("next_smallest_element_n2")
    next_smallest_element_n2(a)

    print("next_smallest_element_fast")
    next_smallest_element_fast(a)