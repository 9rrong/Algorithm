n = int(input())
MOD = 1500000
M = 1000000

dp = [0] * MOD
dp[0] = 0
dp[1] = 1

for i in range(2, MOD):
    dp[i] = (dp[(i - 1)] + dp[(i - 2)]) % M

print(dp[n % MOD])
