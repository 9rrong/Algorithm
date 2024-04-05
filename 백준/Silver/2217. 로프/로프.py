from sys import stdin

N = int(stdin.readline())
rope = []

for _ in range(N):
    rope.append(int(stdin.readline()))

rope.sort(reverse=True)
result = 0

for i in range(N):
    if result <= rope[i] * (i+1):
        result = rope[i] * (i+1)

print(result)