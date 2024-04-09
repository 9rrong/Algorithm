from sys import stdin
import math

N, L = map(int, stdin.readline().split())

pod = [tuple(map(int, stdin.readline().split())) for _ in range(N)]

pod.sort()

last = pod[0][0]
cnt = 0

for start, end in pod:
    if last > end:
        continue
    elif last < start:
        last = start
    count = math.ceil((end - last) / L)
    last += count * L
    cnt += count

print(cnt)