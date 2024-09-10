n = int(input())
ls = list(map(int, input().split()))
x = sorted(set(ls))

res = []
index = dict()

for i in range(len(x)):
    index[x[i]] = i

for i in ls:
    res.append(index[i])

print(' '.join(map(str, res)))