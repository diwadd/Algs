import math
import heapq

class Graph:
    def __init__(self, vertices, adjacency_list):
        self.n_vertices = vertices
        self.adjacency_list = adjacency_list


    def get_minimal_distance(self, dist, s):

        min_val = math.inf

    def dijkstra(self, source_id, t):

        q = []
        heapq.heapify(q)
        dist = [math.inf for i in range(self.n_vertices)]
        dist[source_id] = 0
        prev = [None for i in range(self.n_vertices)]

        heapq.heappush(q, (0, source_id))

        while len(q) != 0:

            u = heapq.heappop(q)
            u_id = u[1]

            if u_id == t:
                break

            print("u_id: {0}".format(u_id))
            for v in self.adjacency_list[u_id]:
                print("len(q): {0} v: {1}".format(len(q), v))
                # We assume that the distance between all vertices is one, i.e., dist(v, u) = 1
                alt = dist[u_id] + 1
                print("alt: {0}".format(alt))
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u_id
                    if v not in q:
                        heapq.heappush(q, (dist[v], v))
        return dist, prev

    def get_path(self, source, target, dist, prev):

        s = []
        u = target

        if (prev[u] is not None) or (u == source):
            while u is not None:
                s.append(u)
                u = prev[u]

        return s


if __name__ == "__main__":
    al = [
          [1, 2, 3],  # 0
          [0, 2],     # 1
          [0, 4],     # 2
          [0, 4, 5],  # 3
          [2, 3, 5],  # 4
          [3, 4, 6, 7, 8],     # 5
          [5, 7, 8],  # 6
          [5, 6, 8],  # 7
          [5, 6, 7]   # 8
          ]

    source = 1
    target = 7

    g = Graph(len(al), al)
    dist, prev = g.dijkstra(source, target)

    print("dist")
    print(dist)

    print("prev")
    print(prev)

    s = g.get_path(source, target, dist, prev)

    print("s")
    print(s)