import copy

class FenwickTree:
    def __init__(self, a):
        n = len(a)
        self.t = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            self.update(i, a[i-1])

    def sum(self, index):
        res = 0
        while index > 0:
            res += self.t[index]
            index -= (index & (-index))
        return res

    def update(self, index, value):
        while index < len(self.t):
            print(f"index: {index}")
            self.t[index] += value
            index += (index & (-index))

    def __str__(self):
        s = ""
        visited = [False for _ in range(len(self.t))]
        for i in range(1, len(self.t)):
            if visited[i] == True:
                continue
            index = copy.deepcopy(i)
            print(f"Printing for index = {index}")
            while index < len(self.t):
                print(f"index: {index}")
                if visited[index] == True:
                    index += (index & (-index))
                    continue
                visited[index] = True
                s = s + f"->{index}/{self.t[index]}"
                index += (index & (-index))
            s = s + "\n"
        return s

if __name__ == "__main__":

    a = [1, 2, 3, 4, 5, 6, 7]
    a = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    ft = FenwickTree(a)

    print(ft.t)
    print(ft)

    for i in range(1, len(a)+1):
        print(ft.sum(i))
    print(f"sum of a: {sum(a)}")