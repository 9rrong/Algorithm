from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    queue = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    depth = 0
    count = 0

    while queue and depth < 2:
        depth += 1
        for _ in range(len(queue)):
            current = queue.popleft()
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    count += 1
    return count


result = bfs(1)
print(result)
