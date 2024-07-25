import sys

input = sys.stdin.readline


def dac(start, end, graph):
    if start == end:
        return graph[end]
    elif end - start == 1:
        if graph[start] < graph[end]:
            return max(graph[start] * 2, graph[end])
        elif graph[end] < graph[start]:
            return max(graph[end] * 2, graph[start])

    mid = (end + start) // 2
    left = dac(start, mid, graph)
    right = dac(mid + 1, end, graph)
    middle, h = graph[mid], graph[mid]
    l, r = mid - 1, mid + 1

    while start <= l and end >= r:
        if graph[l] < graph[r]:
            if graph[r] < h:
                h = graph[r]
            middle = max(middle, (r - l) * h)
            r += 1
        else:
            if graph[l] < h:
                h = graph[l]
            middle = max(middle, (r - l) * h)
            l -= 1

    while r <= end:
        if graph[r] < h:
            h = graph[r]
        middle = max(middle, (r - l) * h)
        r += 1

    while start <= l:
        if graph[l] < h:
            h = graph[l]
        middle = max(middle, (r - l) * h)
        l -= 1

    return max(left, right, middle)


while True:
    graph = list(map(int, input().split()))

    if graph[0] == 0:
        break

    n = graph[0]
    print(dac(1, n, graph))
