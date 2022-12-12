from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # Function to add an edge
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # Function to find the lowest weight spanning tree using Prim's algorithm
    def primMST(self):
        # Initialize the minimum spanning tree
        mst = []

        # Sort the edges in non-decreasing order of weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        # Set of vertices included in the minimum spanning tree
        vertices = set()

        # Add the first vertex to the minimum spanning tree
        vertices.add(self.graph[0][0])
        mst.append(self.graph[0])

        # Loop until all vertices are included in the minimum spanning tree
        while len(vertices) < self.V:
            # Find the minimum weight edge that connects
            # a vertex in the minimum spanning tree
            # to a vertex not in the minimum spanning tree
            for edge in self.graph:
                if edge[0] in vertices and edge[1] not in vertices:
                    vertices.add(edge[1])
                    mst.append(edge)
                    break
                elif edge[1] in vertices and edge[0] not in vertices:
                    vertices.add(edge[0])
                    mst.append(edge)
                    break

        # Print the minimum spanning tree
        for u, v, weight in mst:
            print("%d - %d: %d" % (u, v, weight))
n=int(input("Enter number of vertices: "))
# Create a graph with n vertices
g = Graph(n)

# Ask the user to input the edges and weights of the graph
print("Enter the edges and weights of the graph (u v w):")
while True:
    line = input()
    if line == "":
        break
    u, v, w = map(int, line.split())
    g.addEdge(u, v, w)

# Use Prim's algorithm to find the lowest weight spanning tree
g.primMST()
