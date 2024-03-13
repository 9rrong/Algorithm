from math import inf
from sys import stdin

N, K = map(int, input().split())

graph = [list(map(int, stdin.readline().split())) for _ in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

visited = [False] * N
res = inf
s = []


def dfs(v, s):
    global res

    if len(s) == N - 1:
        res = min(res, sum(s))

    visited[v] = True

    for i in range(N):
        if not visited[i]:
            s.append(graph[v][i])
            dfs(i, s)
            s.pop()
            visited[i] = False


dfs(K, s)

print(res)
