N = int(input())
ls = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i, N):
        if ls[j] > ls[i]:
            dp[j] = max(dp[j],dp[i] + 1)

print(max(dp))


