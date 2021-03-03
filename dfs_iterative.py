# Program to implement depth first search for a given graph using
# iterative algorithm

# Instance of a graph stored as adjacency list using dictionary
# Keys : Nodes
# Values : Neighbours

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []
queue = []

def dfs(graph, start_node, visited):
    print("The nodes with which we are beginning the dfs is", start_node)
    visited.append(start_node)
    print("The initial visited array is ", visited)
    queue.append(start_node)
    print("The queue of nodes to be searched is ", queue )

    while queue:
        search = queue.pop()
        print("The node being searched is ", search)
        for neighbour in graph[search]:
            print("Neighbour of ",search,"being checked is ", neighbour)
            print("Test whether ", neighbour, "is already seen in ", visited)
            if neighbour not in visited:
                visited.append(neighbour)
                print("If not seen, add to the seen ", visited)
                queue.append(neighbour)
                print("Also add it to the list of queue to be searched", queue)

dfs(graph, 'A', visited)