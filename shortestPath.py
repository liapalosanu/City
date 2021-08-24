"""
    Program written in Python3 to find shortest path between two nodes in a
    directed network graph. Algorithm chosen is Dijkstra's.

    Invoke program as follows:

    > python3 getPath.py filename startNode endNode

"""
import sys

# initialise infinite value

INF = 10000000000


def makeGraph(file):
    # graph function to format file into dictionary of dictionaries with parent
    # nodes and child nodes
    parents = {}

    for line in open(file):
        key = line.split()[0]
        parents[key] = {}

    for line in open(file):
        key = line.split()[0]

        if key in parents:
            parents[key][line.split()[1]] = int(line.split()[2])

    return parents


def getPath(graph, start_node, end_node, visited=[], dist={}, predecessors={}):
    # check nodes exist before running algorithm
    if start_node not in graph:
        print("The start node could not be found in graph. Please try "
              "again")
        sys.exit(1)
    if end_node not in graph:
        print("The end node could not be found in graph. Please try "
              "again")
        sys.exit(1)

    if start_node == end_node:
        # get path from set of predecessors

        path = []
        pred = end_node
        while pred is not None:
            path.append(pred)
            pred = predecessors.get(pred, None)

        # print shortest path

        if len(path) <= 1:
            print("No path found")

        else:
            path.reverse()
            print("The Shortest Path is:")
            for node in path:
                print(node)

    else:
        # first run initialises distance of 0 from start_node
        if not visited:
            dist[start_node] = 0
        # visit the neighbors
        for child in graph[start_node]:
            if child not in visited:
                new_distance = dist[start_node] + graph[start_node][child]
                if new_distance < dist.get(child, INF):
                    dist[child] = new_distance
                    predecessors[child] = start_node
        # mark as visited
        visited.append(start_node)
        # after all neighbors have been visited, use recursion
        # new node with smallest value defined stored in x
        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = dist.get(k, INF)
        x = min(unvisited, key=unvisited.get)
        getPath(graph, x, end_node, visited, dist, predecessors)


# commandline setup

if (len(sys.argv)) != 4:
    print("You haven't entered the correct arguments. The syntax is \n"
          "python3 getPath.py filename startNode endNode")
    sys.exit(1)
else:
    file_name = sys.argv[1]
    start = str.capitalize(sys.argv[2])
    end = str.capitalize(sys.argv[3])
    g = makeGraph(file_name)
    getPath(g, start, end)
