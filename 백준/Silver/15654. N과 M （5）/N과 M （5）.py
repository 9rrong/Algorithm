import itertools

n, m = map(int, input().split())

numbers = list(map(int, input().split()))

result = list(itertools.permutations(numbers, m))
result.sort()

for answer in result:
    print(' '.join(map(str, answer)))