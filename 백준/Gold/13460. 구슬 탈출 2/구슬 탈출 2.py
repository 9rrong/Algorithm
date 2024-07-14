from collections import deque

n, m = map(int, input().split())

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

board = [input() for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == "B":
            bsx, bsy = i, j
        elif board[i][j] == "R":
            rsx, rsy = i, j
        elif board[i][j] == "O":
            osx, osy = i, j


def move(x, y, dx, dy):
    distance = 0
    nx, ny = x, y
    while board[nx + dx][ny + dy] != "#" and board[nx][ny] != "O":
        nx += dx
        ny += dy
        distance += 1
    return nx, ny, distance


def bfs():
    visited = set()
    queue = [[rsx, rsy, bsx, bsy, 0]]

    while queue:
        rx, ry, bx, by, cnt = queue.pop(0)
        if cnt == 10:
            return -1

        for (
            dx,
            dy,
        ) in moves:
            rrx, rry, rdis = move(rx, ry, dx, dy)
            bbx, bby, bdis = move(bx, by, dx, dy)

            if board[bbx][bby] != "O":
                if board[rrx][rry] == "O":
                    return cnt + 1
                if rrx == bbx and rry == bby:
                    if rdis > bdis:
                        rrx, rry = rrx - dx, rry - dy
                    else:
                        bbx, bby = bbx - dx, bby - dy

                if (rrx, rry, bbx, bby) in visited:
                    continue
                else:
                    visited.add((rrx, rry, bbx, bby))
                    queue.append([rrx, rry, bbx, bby, cnt + 1])

    return -1


print(bfs())
