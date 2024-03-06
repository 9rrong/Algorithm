from sys import stdin
import heapq

N = int(input())

ls = []
hq = []

for _ in range(N):
    deadline, reward = map(int, stdin.readline().split())
    ls.append((deadline, reward))

ls.sort()

for i in ls:
    heapq.heappush(hq, i[1])
    if len(hq) > i[0]:
        heapq.heappop(hq)

print(sum(hq))
