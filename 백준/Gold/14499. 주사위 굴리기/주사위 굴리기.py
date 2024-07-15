import sys
sys.setrecursionlimit(10**9)

n, m, sx, sy, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))
moves = [(0, 1), (0, -1), (-1, -0), (1, 0)]
dice = {"e": 0, "w": 0, "n": 0, "s": 0, "up": 0, "down": 0}


def roll(direction):
    if direction == 0:
        dice["e"], dice["w"], dice["n"], dice["s"], dice["up"], dice["down"] = (
            dice["down"],
            dice["up"],
            dice["n"],
            dice["s"],
            dice["e"],
            dice["w"],
        )
    elif direction == 1:
        dice["e"], dice["w"], dice["n"], dice["s"], dice["up"], dice["down"] = (
            dice["up"],
            dice["down"],
            dice["n"],
            dice["s"],
            dice["w"],
            dice["e"],
        )
    elif direction == 2:
        dice["e"], dice["w"], dice["n"], dice["s"], dice["up"], dice["down"] = (
            dice["e"],
            dice["w"],
            dice["down"],
            dice["up"],
            dice["n"],
            dice["s"],
        )
    elif direction == 3:
        dice["e"], dice["w"], dice["n"], dice["s"], dice["up"], dice["down"] = (
            dice["e"],
            dice["w"],
            dice["up"],
            dice["down"],
            dice["s"],
            dice["n"],
        )


def move(x, y, cnt):
    direction = command[cnt] - 1
    dx, dy = moves[direction]
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < m:
        roll(direction)
        print(dice["up"])

        if board[nx][ny] == 0:
            board[nx][ny] = dice["down"]
        else:
            dice["down"] = board[nx][ny]
            board[nx][ny] = 0
        x, y = nx, ny

    if cnt < k - 1:
        move(x, y, cnt + 1)


move(sx, sy, 0)
