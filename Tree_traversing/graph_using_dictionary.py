dict={}
Number_of_vertices,edges=map(int,input("Enter the no of vertices and total no of edges:").split())
count=1
while count<=Number_of_vertices:
    vertex=input(f"Enter the {count} vertex:")
    if vertex not in dict:
        dict[vertex]=[]
    else:
        print("you are repeating the vertex")
    count+=1
for i in range(edges):
    vertex,edges=map(str,input("Enter vertex and edge:").split())
    dict[vertex].append(edges)
    dict[edges].append(vertex)
for edges in dict:
    print(edges,dict[edges])
print(dict)