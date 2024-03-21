class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def prim_mst(self):
        mst = [False] * self.V
        key = [float('inf')] * self.V
        parent = [None] * self.V
        key[0] = 0
        parent[0] = -1
        for _ in range(self.V):
            u = min((key[i], i) for i in range(self.V) if not mst[i])[1]
            mst[u] = True
            for v, weight in self.graph[u]:
                if not mst[v] and weight < key[v]:
                    key[v] = weight
                    parent[v] = u
        print("Edges in MST:")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} (Weight: {key[i]})")

# Example usage
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)

g.prim_mst()
