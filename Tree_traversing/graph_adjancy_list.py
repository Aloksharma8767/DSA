class vertex:
    def __init__(self,data):
        self.vertex=data
        self.next=None

class graph:
    def __init__(self,vertices):
        self.NV=vertices
        self.graph_arr=[None]*self.NV

    def add_edges(self,source,destination):
        node=vertex(destination)
        node.next=self.graph_arr[source]
        self.graph_arr[source]=node
        #undirected graph
        node=vertex(source)
        node.next=self.graph_arr[destination]
        self.graph_arr[destination]=node
    
    def print_graph(self):
        for i in range(self.NV):
            print("\n",i,end=" = ")
            temp=self.graph_arr[i]
            while temp is not None:
                print(temp.vertex,end="->")
                temp=temp.next
        print()

#Driver code
if __name__ == "__main__" :
    graph=graph(4)
    graph.add_edges(0,1)
    graph.add_edges(0,3)
    graph.add_edges(1,2)
    graph.add_edges(1,3)
    # graph.add_edges(1,0)
    # graph.add_edges(2,1)
    graph.add_edges(2,3)
    # graph.add_edges(3,0)
    # graph.add_edges(3,1)
    # graph.add_edges(3,2)
    graph.print_graph()