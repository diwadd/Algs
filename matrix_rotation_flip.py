import math

def print_matrix(mt):

    n = len(mt)
    for i in range(n):
        m = len(mt)
        s = ""
        for j in range(m):
            s = s + str(mt[i][j]) + " "
        print(f"{s}")

def matrix_rotation(mt):
    n = len(mt)

    nf = math.floor(n/2)

    for i in range(nf):
        # print(f"i = 0")
        for j in range(i, n-1-i):
            # print(f"[{i}][{j}] [{j}][{n-1-i}] [{n-1-i}][{n-1-j}] [{n-1-j}][{i}]")

            t = mt[i][j]
            mt[i][j] = mt[j][n-1-i]
            mt[j][n-1-i] = mt[n-1-i][n-1-j]
            mt[n-1-i][n-1-j] = mt[n-1-j][i]
            mt[n-1-j][i] = t

    return mt

def visualize_rotation(mt):

    print("Before rotation")
    print_matrix(mt)

    rmt = matrix_rotation(mt)

    print("After rotation")
    print_matrix(rmt)

mt5 = [[1, 2, 3, 1, 2],
       [4, 5, 6, 4, 5],
       [7, 8, 9, 7, 8],
       [2, 4, 6, 8, 0],
       [1, 3, 5, 7, 9]]


mt2 = [[1, 2],
       [3, 4]]

mt3 = [[1, 2, -1],
       [3, 4, -3],
       [7, 8,  9]]

visualize_rotation(mt2)
visualize_rotation(mt5)
visualize_rotation(mt3)

