from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
queue = deque()
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs():

    while queue:
        nxt = queue.popleft()
        visited[nxt] = True

        for i in graph[nxt]:
            if not visited[i]:
                queue.append(i)


queue.append(1)
bfs()

for i in visited:
    if i:
        cnt += 1

print(cnt-1)
