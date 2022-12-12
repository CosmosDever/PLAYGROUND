# graph = {
#     "A": ["B", "G"],
#     "B": ["A","C","G"],
#     "C": ["B","E"],
#     "D": ["F","J","K"],
#     "E": ["G","J","K"],
#     "F": ["D","J","K"],
#     "G": ["A","B","E","J"],
#     "J": ["D","E","F","G"],
#     "K": ["D","E","F"],
#     }

# start = input("Start: ")
# stop = input("Stop: ")
# n = 0

# def dfs_search(start,stop,graph, times = start, path = start):
#     global n
#     if path.count(times) > 1:
#         return
#     if times == stop:
#         final = [i for i in path]
#         if len(final) == len(list(graph.keys())):
#             n += 1
#             print("Answer",n,":",[i for i in path])
#             return
#         else:
#             return
#     for j in graph[times]:
#         dfs_search(start,stop,graph,j,path+j)

# dfs_search(start,stop,graph)
# print("Finished")

# Initialize an empty dictionary
my_dict = {}
key = input("Enter a key: ")
values = []
while True:
    value = input("Enter a value (or press Enter to stop): ")
    if value == "":
        break
    values.append(value)
my_dict[key] = values
print(my_dict)