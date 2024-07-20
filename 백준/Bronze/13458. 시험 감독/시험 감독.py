import math

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

res = 0
res += n
a = [i - b for i in a]

for aa in a:
    if aa < 0:
        aa = 0
    res += math.ceil(aa / c)

print(res)