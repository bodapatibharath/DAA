import sys

def tsp(graph, start):
    n = len(graph)
    
    if n == 1:
        return 0

    
    memo = {}
    
    
    def min_cost(node, visited):
        
        if len(visited) == n:
            return graph[node][start]
        
        
        if (node, tuple(visited)) in memo:
            return memo[(node, tuple(visited))]

        min_distance = sys.maxsize
        
        for next_node in range(n):
            if next_node != node and next_node not in visited:
                visited.add(next_node)
                distance = graph[node][next_node] + min_cost(next_node, visited)
                min_distance = min(min_distance, distance)
                visited.remove(next_node)

        
        memo[(node, tuple(visited))] = min_distance
        return min_distance

    
    return min_cost(start, {start})



n = int(input("Enter the number of nodes: "))
print("Enter the adjacency matrix (separate elements with spaces):")
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


start_node = int(input("Enter the starting node: "))


print("Minimum distance for TSP:", tsp(graph, start_node))
