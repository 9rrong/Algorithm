from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
visited = [False] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs():
    q = deque([1])

    while q:
        nxt = q.popleft()

        for child in graph[nxt]:
            if not visited[child]:
                parent[child] = nxt
                q.append(child)
                visited[child] = True


bfs()

for i in range(2, n + 1):
    print(parent[i])
