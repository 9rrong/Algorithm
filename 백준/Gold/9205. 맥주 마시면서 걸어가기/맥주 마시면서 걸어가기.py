from collections import deque

t = int(input())


def bfs(u):
    queue = deque()
    queue.append(u)

    while queue:
        x, y = queue.popleft()

        for nxt in graph:
            nx, ny = nxt[0], nxt[1]
            if abs(nx - x) + abs(ny - y) <= 1000 and [nx, ny] not in visited:
                queue.append([nx, ny])
                visited.append([nx, ny])


for _ in range(t):
    n = int(input())
    visited = []
    store = []

    home = list(map(int, input().split()))
    for _ in range(n):
        store.append(list(map(int, input().split())))
    festival = list(map(int, input().split()))

    graph = store + [festival]
    bfs(home)

    if festival in visited:
        res = "happy"
    else:
        res = "sad"

    print(res)
