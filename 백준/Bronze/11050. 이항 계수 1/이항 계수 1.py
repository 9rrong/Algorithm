n, k = map(int, input().split())


def factorial(N):
    res = 1
    for i in range(1, N + 1):
        res *= i
    return res


print(int(factorial(n) / (factorial(n - k) * factorial(k))))
