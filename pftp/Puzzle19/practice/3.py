#Programming for the Puzzled -- Srini Devadas
#A Weekend to Remember
#This puzzle deals with the problem of inviting friends to dinner over two days
#such that no two of your friends who dislike each other are invited on the same
#day.  This can be done if the graph is a bipartite graph.

#The code determines if a graph is bipartite or not. If the graph can be colored
#using two colors, it is bipartite, else it is not.

graph = {'B': ['C'],
         'C': ['B', 'D'],
         'D': ['C', 'E', 'F'],
         'E': ['D'],
         'F': ['D', 'G', 'H', 'I'],
         'G': ['F'],
         'H': ['F'],
         'I': ['F']}



def bipartiteGraphColor(graph, start, coloring, color):
    if start not in graph:
        return False, {}
    
    if start not in coloring:
        coloring[start] = color
    elif coloring[start] != color:
        return False, {}
    else:
        return True, coloring
    
    if color == 'Sha':
        newcolor = 'Hat'
    else:
        newcolor = 'Sha'
        
    for vertex in graph[start]:
        val, coloring = bipartiteGraphColor(graph, vertex, coloring, newcolor)
        if val == False:
            return False, {}
        
    return True, coloring

def findPath(graph, start, coloring, end, path):
    if start == end:
        path.append(end)
        return True, coloring, path
    elif :
        return False, coloring, []
    if start not in graph:
        return False, coloring,[]
    
    if start not in coloring:
        coloring.append(start)
        path.append(start)
    else:
        return , coloring, path
    
    for vertex in graph[start]:
        val, coloring, path = findPath(graph, vertex, coloring, end, path)
        if val == False:
            return False, coloring, path

    
    return True,coloring, path
        
    
print (findPath(graph, 'B', [], 'I', []))

