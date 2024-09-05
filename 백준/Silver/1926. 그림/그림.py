from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = 0
num = 0


def bfs(v):
    q = deque([v])
    cnt = 1

    while q:
        x, y = q.popleft()
        graph[x][y] = 0

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1

    return cnt


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ans = max(ans, bfs((i, j)))
            num += 1
print(num)
print(ans)
