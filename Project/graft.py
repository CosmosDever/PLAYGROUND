import sys

# define infinity
INF = sys.maxsize

n=int(input("Enter the number of Vertex: "))
adj_matrix = [[int(i) for i in input().split()] for k in range(n)]
s=int(input("Enter the Start Vertex: "))
d=int(input("Enter the Finish Vertex: "))

def dijkstra(adj_matrix, source, dest):
  # initialize distances and visited arrays
  distances = [INF for i in range(len(adj_matrix))]
  visited = [False for i in range(len(adj_matrix))]

  # set distance of source to 0
  distances[source] = 0

  # while there are unvisited nodes
  while False in visited:
    # find the unvisited node with the smallest distance
    min_distance = INF
    min_index = None
    for i in range(len(adj_matrix)):
      if not visited[i] and distances[i] < min_distance:
        min_distance = distances[i]
        min_index = i
    if min_index is None:
      break

    # update distances of neighbors
    for i in range(len(adj_matrix)):
      if adj_matrix[min_index][i] != 0 and distances[i] > distances[min_index] + adj_matrix[min_index][i]:
        distances[i] = distances[min_index] + adj_matrix[min_index][i]

    # mark the current node as visited
    visited[min_index] = True

    # if destination has been visited, break
    if visited[dest]:
      break

  return distances[dest]
# find the shortest distance from node s to node f
distance = dijkstra(adj_matrix, s, d)
# print the shortest distance from node 0 to node 3
print(distance)  # should output 9