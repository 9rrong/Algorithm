from collections import deque
import sys

input = sys.stdin.readline

W, H = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]
visited = [[0] * W for _ in range(H)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
direction_map = {
    0: (0, 2, 3),
    1: (1, 2, 3),
    2: (0, 1, 2),
    3: (0, 1, 3),
    4: (0, 1, 2, 3),
}

C_positions = [(y, x) for y in range(H) for x in range(W) if grid[y][x] == "C"]
start_y, start_x = C_positions[0]
end_y, end_x = C_positions[1]
min_mirrors = float("inf")
queue = deque([(start_y, start_x, 4, 0)])
visited[start_y][start_x] = 1

while queue:
    y, x, direction, mirrors = queue.popleft()

    if (y, x) == (end_y, end_x):
        min_mirrors = min(min_mirrors, mirrors)
        continue

    for new_direction in direction_map[direction]:
        new_mirrors = mirrors
        ny, nx = y + directions[new_direction][0], x + directions[new_direction][1]

        if direction != new_direction:
            new_mirrors += 1

        while 0 <= ny < H and 0 <= nx < W and grid[ny][nx] != "*":
            if not visited[ny][nx]:
                visited[ny][nx] = new_mirrors
                queue.append((ny, nx, new_direction, new_mirrors))
            ny += directions[new_direction][0]
            nx += directions[new_direction][1]

print(min_mirrors - 1)
