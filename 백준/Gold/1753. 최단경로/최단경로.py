import sys, heapq

input = sys.stdin.readline


INF = 10**6
V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)
K = int(input())
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = i[1] + dist

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(K)

for i in range(1, V + 1):
    print(distance[i] if distance[i] < 1000000 else "INF")
