from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    # Function to add an edge
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to perform DFS on the graph
    def dfs(self, origin):
        # Initialize the visited set and the path
        visited = set()
        path = []

        # Recursive helper function to perform DFS
        def dfsUtil(v):
            visited.add(v)
            path.append(v)
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    dfsUtil(neighbor)

        # Start the DFS traversal from the given origin vertex
        dfsUtil(origin)

        # Return the path
        return path

n=int(input("Enter number of vertices: "))
# Create a graph with n vertices
g = Graph(n)

# Ask the user to input the edges of the graph
print("Enter the edges of the graph (u v):")
while True:
    line = input()
    if line == "":
        break
    u, v = map(int, line.split())
    g.addEdge(u, v)

# Ask the user to input the origin vertex
origin = int(input("Enter the origin vertex:"))

# Use DFS to find a tree-spreading path starting from the given origin vertex
path = g.dfs(origin)

# Print the path
print("Tree-spreading path:", " ".join(map(str, path)))
