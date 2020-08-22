n, m, v = map(int, input().split())

graph = []
for i in range(m):
    graph = [[0] * (n + 1) for i in range(n + 1)]

for i in range(m):
    x, y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1
print(graph)


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end= " ")

    for i in range(1, n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(graph, i, visited)

visited = [False] * (n + 1)

dfs(graph, v, visited)