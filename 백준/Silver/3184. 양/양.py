import sys
sys.setrecursionlimit(10**6)

R, C = map(int, input().split())
yard = [list(input()) for _ in range(R)]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
s = []
m = []
res_o = 0
res_v = 0


def dfs(x, y, s):
    if yard[x][y] != "#" and yard[x][y] != "0":
        s.append(yard[x][y])

        yard[x][y] = "0"
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and yard[nx][ny] != "#" and yard[nx][ny] != "0":
                dfs(nx, ny, s)


for i in range(R):
    for j in range(C):
        s = []
        dfs(i, j, s)
        if s:
            m.append("".join(map(str, s)))

for group in m:
    v = group.count("v")
    o = group.count("o")
    if o > v:
        res_o += o
    else:
        res_v += v


print(res_o, res_v)
