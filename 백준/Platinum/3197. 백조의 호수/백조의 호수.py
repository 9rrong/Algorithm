import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
lake = [list(input().rstrip()) for _ in range(r)]
moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]
swan = []
water_queue = deque()
swan_queue = deque()
next_water_queue = deque()
next_swan_queue = deque()
result = 0

for i in range(r):
    for j in range(c):
        if lake[i][j] == 'L':
            swan.append((i, j))
            lake[i][j] = '.'
        if lake[i][j] == '.':
            water_queue.append((i, j))

swan_start, swan_end = swan
swan_queue.append(swan_start)
visited = [[False] * c for _ in range(r)]
visited[swan_start[0]][swan_start[1]] = True

def melt():
    while water_queue:
        rr, cc = water_queue.popleft()
        for dr, dc in moves:
            nr, nc = rr + dr, cc + dc
            if 0 <= nr < r and 0 <= nc < c and lake[nr][nc] == 'X':
                lake[nr][nc] = '.'
                next_water_queue.append((nr, nc))

def can_meet():
    while swan_queue:
        rr, cc = swan_queue.popleft()
        if (rr, cc) == swan_end:
            return True
        for dr, dc in moves:
            nr, nc = rr + dr, cc + dc
            if 0 <= nr < r and 0 <= nc < c and not visited[nr][nc]:
                visited[nr][nc] = True
                if lake[nr][nc] == '.':
                    swan_queue.append((nr, nc))
                elif lake[nr][nc] == 'X':
                    next_swan_queue.append((nr, nc))
    return False

while True:
    if can_meet():
        break
    melt()
    water_queue = next_water_queue
    next_water_queue = deque()
    swan_queue = next_swan_queue
    next_swan_queue = deque()
    result += 1

print(result)
