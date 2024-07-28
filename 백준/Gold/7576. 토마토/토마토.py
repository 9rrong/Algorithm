from collections import deque

M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]

cnt = -1
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
changed = True
q = deque()
nq = deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            nq.append((i, j))

while changed:
    cnt += 1
    while nq:
        q.append(nq.popleft())

    changed = False

    while q:
        r, c = q.popleft()

        for dr, dc in moves:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < M and box[nr][nc] == 0:
                box[nr][nc] = 1
                changed = True
                nq.append((nr, nc))

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            cnt = -1

print(cnt)
