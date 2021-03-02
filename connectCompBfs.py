# Program to find the number of connected components of a graph

# Instance of a graph stored as adjacency list using dictionary
# Keys : Nodes
# Values : Neighbours

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['G'],
    'G': [],
    'H': [],
    'I': ['J'],
    'J': []

}


def ccbfs(graph, start_node):
    vertices = graph.keys()
    explored = []
    queue = [start_node]
    cc = 0
    for index, node in enumerate(vertices):
        if node not in explored:
            cc += 1
            while queue:
                search = queue.pop(0)
                for neighbors in graph[search]:
                    if neighbors not in explored:
                        explored.append(neighbors)
                        queue.append(neighbors)
    return  cc

comp = ccbfs(graph, 'A')
print(comp)






