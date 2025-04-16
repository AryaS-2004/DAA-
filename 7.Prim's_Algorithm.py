# Taking user input for adjacency matrix with validation
num_vertices = int(input("Enter number of vertices: "))

if num_vertices <= 0:
    print("Invalid number of vertices. Exiting...")
    exit()

graph = []
print("Enter adjacency matrix (use 0 for no edge):")

for i in range(num_vertices):
    row = input().split()
    if len(row) != num_vertices:
        print("Invalid matrix row length. Exiting...")
        exit()
    graph.append(list(map(int, row)))

# Compute MST using Prim's algorithm
min_cost, mst_edges = prim_mst(graph)

# Display Results
print("\nMinimum Cost Spanning Tree (MST) Edges:")
for u, v, w in mst_edges:
    print(f"Edge ({u} - {v}) with weight {w}")

print("Total Minimum Cost of MST:", min_cost)
