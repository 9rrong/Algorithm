from collections import deque

M, N, H = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()


def bfs():
    while queue:
        z, y, x = queue.popleft()

        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if arr[nz][ny][nx] == 0:
                    arr[nz][ny][nx] = arr[z][y][x] + 1
                    queue.append([nz, ny, nx])


for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                queue.append([i, j, k])

bfs()

imp = False
result = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                imp = True
            result = max(result, arr[i][j][k])

if imp:
    print(-1)
else:
    print(result-1)