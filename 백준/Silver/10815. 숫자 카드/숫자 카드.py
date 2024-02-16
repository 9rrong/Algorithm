from sys import stdin

N = int(stdin.readline())
A = sorted(map(int, stdin.readline().split()))
M = int(stdin.readline())
B = map(int, stdin.readline().split())


def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start + end) // 2

    if A[m] == l:
        return 1
    elif A[m] > l:
        return binary(l, N, start, m - 1)
    elif A[m] < l:
        return binary(l, N, m + 1, end)


for l in B:
    start = 0
    end = N - 1
    print(binary(l, N, start, end), end=" ")
