from collections import deque

N = int(input())
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(u):
    sr, sc = u
    queue = deque([(sr, sc)])
    cnt = [[-1] * (w + 2) for _ in range(h + 2)]
    cnt[sr][sc] = 0

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            dr, dc = moves[i]
            nr, nc = r + dr, c + dc

            if 0 <= nr < h + 2 and 0 <= nc < w + 2 and cnt[nr][nc] == -1:
                if prison[nr][nc] == ".":
                    cnt[nr][nc] = cnt[r][c]
                    queue.appendleft((nr, nc))
                elif prison[nr][nc] == "#":
                    cnt[nr][nc] = cnt[r][c] + 1
                    queue.append((nr, nc))
    return cnt


for _ in range(N):
    h, w = map(int, input().split())
    prison = (
        [["."] * (w + 2)]
        + [["."] + list(input()) + ["."] for _ in range(h)]
        + [["."] * (w + 2)]
    )
    starts = [(0, 0)]
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if prison[i][j] == "$":
                starts.append((i, j))
                prison[i][j] = "."

    cnt1 = bfs(starts[0])
    cnt2 = bfs(starts[1])
    cnt3 = bfs(starts[2])

    ans = float("inf")

    for i in range(h):
        for j in range(w):
            if cnt1[i][j] != -1 and cnt2[i][j] != -1 and cnt3[i][j] != -1:
                if prison[i][j] == ".":
                    ans = min(ans, cnt1[i][j] + cnt2[i][j] + cnt3[i][j])
                elif prison[i][j] == "#":
                    ans = min(ans, cnt1[i][j] + cnt2[i][j] + cnt3[i][j] - 2)
    print(ans)
