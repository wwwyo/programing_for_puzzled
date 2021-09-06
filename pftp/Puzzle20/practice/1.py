#Programming for the Puzzled -- Srini Devadas
#Six Degrees of Separation
#Use Breadth-First Search to find shortest paths in a graph
#These shortest paths are used to determine degree of separation between vertices
#If the procedure is run with all possible start vertices, the degree of
#separation of the graph can be found

#Exercise 1: Write a procedure to determine the degree of separation
#of a pair of vertices.  Use the procedure to find the degree of separation
#of the graph by running it on each pair of vertices.

small = {'A': ['B', 'C'],
         'B': ['A', 'C', 'D'],
         'C': ['A', 'B', 'E'],
         'D': ['B', 'E'],
         'E': ['C', 'D', 'F'],
         'F': ['E']}

large = {'A': ['B', 'C', 'E'], 'B': ['A', 'C'], 'C': ['A', 'B', 'J'],
         'D': ['E', 'F', 'G'], 'E': ['A', 'D', 'K'], 'F': ['D', 'N'],
         'G': ['D', 'H', 'I'], 'H': ['G', 'M'], 'I': ['G', 'P'],
         'J': ['C', 'K', 'L'], 'K': ['E', 'J', 'L'], 'L': ['J', 'K', 'S'],
         'M': ['H', 'N', 'O'], 'N': ['F', 'M', 'O'], 'O': ['N', 'M', 'V'],
         'P': ['I', 'Q', 'R'], 'Q': ['P', 'W'], 'R': ['P', 'X'],
         'S': ['L', 'T', 'U'], 'T': ['S', 'U'], 'U': ['S', 'T', 'V'],
         'V': ['O', 'U', 'W'], 'W': ['Q', 'V', 'Y'], 'X': ['R', 'Y', 'Z'],
         'Y': ['W', 'X', 'Z'], 'Z': ['X', 'Y']}
    
#This procedure finds the shortest distance between a start vertex and an end vertex.
#It does this using breadth-first search.



#This procedure computes the degree of separation for each pair of
#vertices in the given graph and reports the maximum number


def degreesOfSeparationVertices(graph, start, end):
    if start not in graph:
        return None
    
    visited = set()
    frontier = set()
    degrees = 0

    visited.add(start)
    frontier.add(start)
    while len(frontier) > 0:
        for visit in frontier:
            if visit == end:
                return degrees
            for node in graph[visit]:
                new_frontier = set()
                if not node in visited:
                    visited.add(node)
                    new_frontier.add(node)
        frontier = new_frontier
        degrees += 1

    return None

def graphDegreeOfSeparation(graph):
    max_degrees = 0
    for g in graph.keys():
        for h in graph.keys():
            degrees = 0
            if g != h:
                degrees = degreesOfSeparationVertices(graph, g, h)
                if degrees != None:
                    max_degrees = max(max_degrees, degrees)
    print(max_degrees)

print(degreesOfSeparationVertices(small, 'A', 'E'))
graphDegreeOfSeparation(large)




