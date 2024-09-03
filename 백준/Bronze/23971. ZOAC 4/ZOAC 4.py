h, w, n, m = map(int, input().split())

print((1 + ((h - 1) // (n + 1))) * (1 + ((w - 1) // (m + 1))))
