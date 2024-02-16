from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int, stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int, stdin.readline().split()))

h = {}

for i in card:
    if i in h:
        h[i] += 1
    else:
        h[i] = 1

for i in test:
    if i in h:
        print(h[i], end=" ")
    else:
        print(0, end=" ")
