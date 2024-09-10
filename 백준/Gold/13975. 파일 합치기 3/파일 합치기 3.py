import heapq
import copy
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    tmp = []
    heapq.heapify(files)
    res = 0

    while len(files) > 1:
        a = heapq.heappop(files)
        b = heapq.heappop(files)
        heapq.heappush(files, a + b)
        res += a + b

    print(res)
