n = int(input())
graph = []
white = 0
blue = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))


def check(x, y, size):
    is_blue = True
    global blue, white

    half = size // 2

    if graph[x][y] == 0:
        is_blue = False

    if is_blue:
        for i in range(x, x + size):
            for j in range(y, y + size):
                if graph[i][j] != 1:
                    check(x, y, half)
                    check(x + half, y, half)
                    check(x, y + half, half)
                    check(x + half, y + half, half)
                    return
        blue += 1

    if not is_blue:
        for i in range(x, x + size):
            for j in range(y, y + size):
                if graph[i][j] != 0:
                    check(x, y, half)
                    check(x + half, y, half)
                    check(x, y + half, half)
                    check(x + half, y + half, half)
                    return
        white += 1
    return


check(0, 0, n)


print(white)
print(blue)
