n = int(input())
s = [0] + [list(map(int, input().split())) for _ in range(n)]
max_result = 0


def dfs(u, result):
    global max_result

    if u > n:
        max_result = max(result, max_result)
        return

    t, p = s[u][0], s[u][1]

    dfs(u + 1, result)

    if u + t <= n + 1:
        dfs(u + t, result + p)


dfs(1, 0)
print(max_result)
