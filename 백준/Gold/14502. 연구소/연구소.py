from collections import deque
import copy

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
result = 0


def block(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                block(cnt + 1)
                board[i][j] = 0


def bfs():
    global result

    queue = deque()
    b = copy.deepcopy(board)

    for i in range(n):
        for j in range(m):
            if b[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            dx, dy = moves[i]
            nx, ny = x + dx, y + dy

            if n > nx >= 0 and 0 <= ny < m and b[nx][ny] == 0:
                b[nx][ny] = 2
                queue.append((nx, ny))

    cnt = sum(row.count(0) for row in b)
    result = max(result, cnt)


block(0)
print(result)
