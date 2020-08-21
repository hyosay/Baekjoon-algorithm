n, m, v = map(int, input().split())

graph = []
for i in range(m):
    graph.append(sorted(list(map(int, input().split()))))
graph.insert(0, [])
print(graph)
#dfs
def dfs(graph, d, visited):
    visited[d] = True
    print(d, end = ' ')

    for i in graph[d]:
        if not visited[i]:
            dfs(graph, i, visited)




visited = [False] * (m + 1)
dfs(graph, v, visited)