from sys import stdin

a, b, c = map(int, stdin.readline().split())


def dac(a, b):
    if b == 1:
        return a % c

    tmp = dac(a, b // 2)

    if b % 2 == 0:
        return tmp * tmp % c
    else:
        return tmp * tmp * a % c


print(dac(a, b))
