import sys

class Vertex:

    def __init__(self, key):
        self.key = key
        self.p = None
        self.r = None

    #def __str__(self):
    #    s = str(self.key)
    #    for i in range(len(self.edges)):
    #        s = s + " -> " + str(self.edges[i])
    #    return s

    def __str__(self):
        s = "Vertex: (" + str(self.key) + ")"
        return s

    def __eq__(self, other):

        if isinstance(other, Vertex) == False:
            return False
        elif (self.key == other.key):
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


class Edge:

    def __init__(self, u, v):
        self.u = u
        self.v = v


class Graph:

    def __init__(self, vertex_list, edge_list):
        self.vertex_list = vertex_list
        self.nv = len(vertex_list)

        self.edge_list = edge_list
        self.ne = len(edge_list)


    def print_graph(self):
        for i in range(self.nv):
            s = str(self.vertex_list[i])
            for j in range(self.ne):
                if (self.edge_list[j].u == self.vertex_list[i].key):
                    s = s + " -> " + str(self.edge_list[j].v)
                elif (self.edge_list[j].v == self.vertex_list[i].key):
                    s = s + " -> " + str(self.edge_list[j].u)
                else:
                    continue
            print(s)



class DisjointSetObject:
    def __init__(self, p, r):
        self.p = p # parent
        self.r = r # rank

    def __eq__(self, other):
        if self.p == other.p:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


def make_set(v):
    v.p = v
    v.r = 0


def link(x, y):
    if x.r > y.r:
        y.p = x
    else:
        x.p = y
        if x.r == y.r:
            y.r = y.r + 1

def find_set(x):
    if x != x.p:
        x.p = find_set(x.p)
    return x.p

def union(x, y):
    link( find_set(x), find_set(y) )


def connected_components(g):
    
    for i in range(g.nv):
        make_set(g.vertex_list[i])
    for i in range(g.ne):
        e = g.edge_list[i]

        if find_set(g.vertex_list[e.u]) != find_set(g.vertex_list[e.v]):
            union(g.vertex_list[e.u], g.vertex_list[e.v])


def same_component(u, v):

    if find_set(u) == find_set(v):
        return True
    else:
        return False


def print_set(v):

    if v.p != None:
        print(v)
        print_set(v.p)
    elif v.p == None:
        print("No more elements in set")
    else:
        # This part of the if statement
        # should be never reached.
        # If it is reached then something is very wrong.
        sys.exit("ERROR! In print_set, reached else.")
        



if (__name__ == "__main__"):
    print("Disjoint sets...")

    vertex_list = [Vertex(i) for i in range(10)]

    edge_list = [Edge(0, 1),
                 Edge(0, 2),
                 Edge(1, 2),
                 Edge(1, 3),
                 Edge(4, 5),
                 Edge(4, 6),
                 Edge(7, 8)]


    print(vertex_list[0] == vertex_list[0])
    print(vertex_list[0] == vertex_list[1])

    print(vertex_list[0] != vertex_list[0])
    print(vertex_list[0] != vertex_list[1])

    print(vertex_list[0] == 1)
    print(vertex_list[0] == None)

    g = Graph(vertex_list, edge_list)
    g.print_graph()

    connected_components(g)
    
    print("After connecting the components:")
    g.print_graph()

    u = g.vertex_list[5]
    v = g.vertex_list[1]
    print(same_component(u, v))

    print("Keys: ")
    print(g.vertex_list[4].key)
    print(g.vertex_list[5].key)
    print(g.vertex_list[6].key)
    print("Ranks: ")
    print(g.vertex_list[4].r)
    print(g.vertex_list[5].r)
    print(g.vertex_list[6].r)
    print("p.Keys: ")
    print(g.vertex_list[4].p.key)
    print(g.vertex_list[5].p.key)
    print(g.vertex_list[6].p.key)
    print("p.Ranks: ")
    print(g.vertex_list[4].p.r)
    print(g.vertex_list[5].p.r)
    print(g.vertex_list[6].p.r)

    print("9:")
    print(g.vertex_list[9].key)
    print(g.vertex_list[9].r)
    print(g.vertex_list[9].p.key)
    print(g.vertex_list[9].p.r)






