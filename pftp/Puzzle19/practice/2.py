#Programming for the Puzzled -- Srini Devadas
#A Weekend to Remember
#This puzzle deals with the problem of inviting friends to dinner over two days
#such that no two of your friends who dislike each other are invited on the same
#day.  This can be done if the graph is a bipartite graph.

#The code determines if a graph is bipartite or not. If the graph can be colored
#using two colors, it is bipartite, else it is not.



graphc = {'A': ['B', 'D', 'C'],
        'B': ['C', 'A', 'B'],
        'C': ['D', 'B', 'A'],
        'D': ['A', 'C', 'B']}

def bipartiteGraphColor(graph, start, coloring, color, oList):
    if start not in graph:
        return False, {}, oList
    
    if start not in coloring:
        coloring[start] = color
        oList.append(start)
    elif coloring[start] != color:
        oList.append(start)
        return False, {}, oList
    else:
        return True, coloring, oList
    
    if color == 'Sha':
        newcolor = 'Hat'
    else:
        newcolor = 'Sha'
        
    for vertex in graph[start]:
        val, coloring, oList = bipartiteGraphColor(graph, vertex, coloring, newcolor, oList)
        if val == False:
            return False, {}, oList
        
    return True, coloring, oList

print(bipartiteGraphColor(graphc, 'A', {}, 'Sha', []))
# print (bipartiteGraphColor(graph, 'B', {}, 'Sha'))
# print (bipartiteGraphColor(graph2, 'B', {}, 'Sha'))
# print (bipartiteGraphColor(grap, 'A', {}, 'Sha'))
