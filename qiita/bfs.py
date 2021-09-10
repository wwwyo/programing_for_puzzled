graph = {'A': ['B', 'D'],
        'B': ['C', 'A'],
        'C': ['D', 'B'],
        'D': ['A', 'C']}

def bfs(graph, start, memo = {}):
    visited = set()
    frontear = set()
    step = 0

    frontear.add(start)

    while len(frontear) > 0:
        new_frontear = set()
        for node in frontear:
            if not node in visited:
                visited.add(node)
                if step in memo:
                    memo[step] += [node]
                else:
                    memo[step] = [node]
                for child_node in graph[node]:
                    new_frontear.add(child_node)

        frontear = new_frontear
        step += 1
    return memo

root = 'A'
print(bfs(graph, root))