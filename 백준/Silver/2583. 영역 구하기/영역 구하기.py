M, N, K = map(int, input().split())
graph = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = []


def dfs(x, y):
    stack = [(x, y)]
    area_size = 0

    while stack:
        cx, cy = stack.pop()
        if graph[cx][cy] == 0:
            graph[cx][cy] = 1
            area_size += 1

            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]

                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                    stack.append((nx, ny))

    return area_size


for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            area_size = dfs(i, j)
            res.append(area_size)

res.sort()
print(len(res))
print(" ".join(map(str, res)))
