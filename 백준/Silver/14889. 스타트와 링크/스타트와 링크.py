n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
result = float("inf")


def dfs(a, idx):
    global result

    if a == n // 2:
        start, link = 0, 0

        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += graph[i][j]
                elif not visited[i] and not visited[j]:
                    link += graph[i][j]

        result = min(result, abs(start - link))
        return
    else:
        for i in range(idx, n):
            if not visited[i]:
                visited[i] = True
                dfs(a + 1, i + 1)
                visited[i] = False


dfs(0, 0)
print(result)
