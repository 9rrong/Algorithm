from collections import deque

dp = [10**9] * 100001
n, k = map(int, input().split())
dp[n] = 0

queue = deque([n])

while queue:
    i = queue.popleft()
    if i - 1 >= 0:
        if dp[i - 1] > dp[i] + 1:
            dp[i - 1] = dp[i] + 1
            queue.append(i - 1)
    if i + 1 <= 100000:
        if dp[i + 1] > dp[i] + 1:
            dp[i + 1] = dp[i] + 1
            queue.append(i + 1)
    if i * 2 <= 100000:
        if dp[i * 2] > dp[i]:
            dp[i * 2] = dp[i]
            queue.append(i * 2)

print(dp[k])
