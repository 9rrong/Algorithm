import sys

input = sys.stdin.readline

n, k = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(k + 1)]

for w, v in wv:
    for i in range(k, 0, -1):
        if i >= w:
            dp[i] = max(dp[i], dp[i - w] + v)

print(dp[k])
