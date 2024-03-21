def floyd(graph):
    n = len(graph)
    
    dist = [row[:] for row in graph]

    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


n = int(input("Enter the number of vertices in the graph: "))
print("Enter the weighted adjacency matrix (use 'inf' for infinity):")
graph = []
for _ in range(n):
    row = input().split()
    for i in range(n):
        if row[i] == 'inf':
            row[i] = float('inf')
        else:
            row[i] = int(row[i])
    graph.append(row)


shortest_paths = floyd(graph)


print("Shortest paths between all pairs of vertices:")
for row in shortest_paths:
    print(row)
