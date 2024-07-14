import sys
sys.setrecursionlimit(10**9)

n = int(input())
k = int(input())

apple = [list(map(int, input().split())) for _ in range(k)]
rotation = {}
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]


l = int(input())

for _ in range(l):
    a, b = input().split()
    rotation[int(a)] = b


def move(x, y, direction, time, tail):
    dx, dy = moves[direction]
    nx, ny = x + dx, y + dy

    if [nx, ny] in tail or nx < 1 or nx > n or ny < 1 or ny > n:
        return time

    if [ny, nx] in apple:
        tail.append([x, y])
        apple.remove([ny, nx])

    else:
        tail.append([x, y])
        tail.pop(0)

    if rotation.get(time) == "D":
        direction = (direction + 5) % 4
    elif rotation.get(time) == "L":
        direction = (direction + 3) % 4

    return move(nx, ny, direction, time + 1, tail)


print(move(1, 1, 0, 1, []))
