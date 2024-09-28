# Input for number of vertices
n = int(input("Enter the number of vertices: "))

# Input for vertices (space-separated)
vertices = list(map(int, input("Enter the vertices (space-separated): ").split()))

# Input for number of edges
num_edges = int(input("Enter the number of edges: "))

# Input for edges (each pair space-separated, e.g., "0 1")
edges = []
for _ in range(num_edges):
    u, v = map(int, input("Enter edge (space-separated pair): ").split())
    edges.append((u, v))

# Initialize an n x n matrix with all zeros
adj_matrix = [[0] * n for _ in range(n)]

# Fill the adjacency matrix based on the edges
for edge in edges:
    u, v = edge
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1  # For undirected graph, mark both [u][v] and [v][u]

# Print the adjacency matrix
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)
