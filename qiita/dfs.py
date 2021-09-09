graph = {'A': ['B', 'D'],
        'B': ['C', 'A'],
        'C': ['D', 'B'],
        'D': ['A', 'C']}

def changeColor(color):
    if color == 'red':
        return 'blue'
    else:
        return 'red'

def dfs(graph, start, color, memo = {}):
    if not start in memo:
        memo[start] = color
        color = changeColor(color)
    else:
        if memo[start] == color:
            color = changeColor(color)
            return True
        else:
            return False

    for node in graph[start]:
        result = dfs(graph, node, color, memo)
        if not result:
            return '二部グラフじゃない！'

    return '二部グラフ！！！'

root = 'A'
color = 'red'
print(dfs(graph, root, color))