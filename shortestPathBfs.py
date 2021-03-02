# Program to implement shortest path using breadth first search

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
    'G': []
}


# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]

    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"

    # keeps looping until all possible paths have been checked
    while queue:
        print("The paths are ", queue)
        # pop the first path from the queue
        path = queue.pop(0)
        print("The path being containing the node being checked")
        # get the last node from the path
        node = path[-1]
        print("The node ",node, "neighbours are being searched now.")
        if node not in explored:
            print("See all the neighbours of the node")
            neighbours = graph[node]
            # go through all neighbour nodes
            # construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as explored
            explored.append(node)

    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("


sp = bfs_shortest_path(graph, 'A', 'D')  # returns ['G', 'C', 'A', 'B', 'D']
print(sp)
print("The number of edges between given path is", len(sp))