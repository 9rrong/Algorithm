from sys import stdin
import heapq

input = stdin.readline

heap = []

n = int(input())

for _ in range(n):
    num = int(input())

    if num == 0:
        if heap:
            print(heapq.heappop(heap) * (-1))
        else:
            print(0)
    else:
        heapq.heappush(heap, -num)