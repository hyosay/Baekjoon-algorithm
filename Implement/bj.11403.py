N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            graph[j][i] = 1

count = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count += 1
count = count // 2

visited = [0] * count
def dfs(v):

    visited[v] = 1
    print(v, end= ' ')

    for i in range(0, N):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)

dfs(1)