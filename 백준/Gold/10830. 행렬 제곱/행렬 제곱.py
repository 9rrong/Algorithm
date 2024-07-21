n, b = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
MOD = 1000


def multiplication_mod(A, B):
    res = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            res[row][col] = sum(A[row][i] * B[i][col] for i in range(n)) % MOD
    return res


def power_mod(A, B):
    if B == 1:
        for i in range(n):
            for j in range(n):
                A[i][j] %= MOD
        return A

    tmp = power_mod(A, B // 2)
    if B % 2 == 0:
        return multiplication_mod(tmp, tmp)
    else:
        return multiplication_mod(A, multiplication_mod(tmp, tmp))


for i in range(n):
    result = power_mod(graph, b)
    print(" ".join(map(str, result[i])))
