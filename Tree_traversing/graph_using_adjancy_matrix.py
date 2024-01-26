#IT TAKES ALPHABEATS AS A INPUT
def printmatrix(matrix):
    r,c=len(matrix),len(matrix[0])
    for i in range(r):
        for j in range(c):
            print(matrix[i][j],end=" ")
        print()
v,e=map(int,input().split())
matrix=[[0]*v for i in range(v)]
for i in range(e):
    u,v=map(str,input().split())
    u=ord(u)-ord("A")
    v=ord(v)-ord("A")
    matrix[u][v]=1
    matrix[v][u]=1
printmatrix(matrix)

#IT TAKES INTEGERS AS A INPUT
def create_adjacency_matrix(vertices, edges):
    # Initialize a square matrix filled with zeros
    matrix = [[0] * vertices for _ in range(vertices)]

    # Fill the matrix based on the edges
    for edge in edges:
        src, dest = edge
        matrix[src][dest] = 1
        matrix[dest][src] = 1  # Assuming an undirected graph

    return matrix

# Example usage:
vertices,Total_edges=map(int,input("Enter total vertices and no of edges:").split())
edges=[]
while Total_edges!=0:
    a, b = map(str,(input("Enter two values: ")).split())
    edges.append((a,b))
    Total_edges-=1

adjacency_matrix = create_adjacency_matrix(vertices, edges)
# Print the adjacency matrix
for row in adjacency_matrix:
    print(row)


