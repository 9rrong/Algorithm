from collections import deque
import sys

input = sys.stdin.readline


def bfs(s):
    visited = [False] * (n + 1)
    q = deque([s])
    visited[s] = True
    cnt = 1
    while q:
        w = q.popleft()
        for v in graph[w]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
                cnt += 1
    return cnt


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


maxCnt = 0
maxCom = []
for i in range(1, n + 1):
    cnt = bfs(i)
    if maxCnt < cnt:
        maxCnt = cnt
        maxCom = [i]
    elif maxCnt == cnt:
        maxCom.append(i)

print(*maxCom)
