class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def is_safe(self, v, pos, path):
        return self.graph[path[pos-1]][v] == 1 and v not in path

    def hamiltonian_circuit_util(self, path, pos):
        if pos == self.V:
            return self.graph[path[pos-1]][path[0]] == 1
        for v in range(1, self.V):
            if self.is_safe(v, pos, path):
                path[pos] = v
                if self.hamiltonian_circuit_util(path, pos+1):
                    return True
                path[pos] = -1
        return False

    def hamiltonian_circuit(self):
        path = [-1] * self.V
        path[0] = 0
        if not self.hamiltonian_circuit_util(path, 1):
            print("Hamiltonian Circuit does not exist")
            return False
        print("Hamiltonian Circuit exists and the following is the path:")
        print(*path, path[0])
        return True
if __name__ == "__main__":
    g1 = Graph(5)
    g1.graph = [[0, 1, 0, 1, 0],
                [1, 0, 1, 1, 1],
                [0, 1, 0, 0, 1],
                [1, 1, 0, 0, 1],
                [0, 1, 1, 1, 0]]
    g1.hamiltonian_circuit()
