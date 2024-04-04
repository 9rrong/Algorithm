from sys import stdin
from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
cnt = 0
result = []

for _ in range(m):
    x, y = map(int, stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)


def dfs(v, cnt):
    cnt += 1
    visited[v] = True

    if v == b:
        result.append(cnt)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, cnt)


dfs(a, cnt)

if result:
    print(result[-1]-1)
else:
    print(-1)
