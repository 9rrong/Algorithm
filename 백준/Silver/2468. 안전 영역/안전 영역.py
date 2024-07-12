import sys

sys.setrecursionlimit(10**9)

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
res = 0


def dfs(x, y, h):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if n > nx >= 0 and n > ny >= 0 and not visited[nx][ny] and graph[nx][ny] > h:
            dfs(nx, ny, h)


height = max(map(max, graph))

for h in range(height + 2):
    visited = [[False] * n for _ in range(n)]
    res = max(res, cnt)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > h:
                dfs(i, j, h)
                cnt += 1

print(res)
