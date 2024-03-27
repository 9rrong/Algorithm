from sys import stdin
from collections import deque

N, M = map(int, input().split())

arr = [list(map(int, " ".join(stdin.readline().split()))) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1:
                    queue.append((nx, ny))
                    arr[nx][ny] = arr[x][y] + 1


bfs()
print(arr[N - 1][M - 1])
