P = int(input())


def fibonacci_mod(m):
    cnt, first, second = 0, 0, 1

    while True:
        tmp = first % m + second % m
        first, second = second, tmp
        if cnt > 0 and (first, second) == (1, 1):
            return cnt
        cnt += 1


for _ in range(P):
    N, M = map(int, input().split())
    print(N, fibonacci_mod(M))
