n, m = map(int, input().split())
a, b = set(), set()

for _ in range(n):
    a.add(input())

for _ in range(m):
    b.add(input())

c = a & b

print(len(c))

d = list(c)
d.sort()

for res in d:
    print(res)