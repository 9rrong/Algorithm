n, m = map(int, input().split())
di = dict()

for i in range(1, n+1):
    name = input()
    di[name] = str(i)
    di[str(i)] = name

for _ in range(m):
    print(di[input()])