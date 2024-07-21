n, k = map(int, input().split())
MOD = 1000000007


def factorial_mod(n):
    res = 1
    for i in range(2, n + 1):
        res = (res * i) % MOD
    return res


def pow_mod(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n

    half = pow_mod(n, k // 2)

    if k % 2 == 0:
        return half * half % MOD
    else:
        return n * half * half % MOD


print(
    pow_mod(factorial_mod(k) * factorial_mod(n - k), MOD - 2) * factorial_mod(n) % MOD
)
