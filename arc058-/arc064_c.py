from heapq import heappop, heappush


def dijkstra(S, N):
    DIST = [pow(10, 10)] * N
    DIST[S] = 0

    que = [(DIST[S], S)]
    while que:
        d, q = heappop(que)
        if DIST[q] < d:
            continue
        for i, d_qi in enumerate(cost[q]):
            tmp = d + d_qi
            if DIST[i] > tmp:
                DIST[i] = tmp
                heappush(que, (tmp, i))
    return DIST[-1]


sx, sy, tx, ty = map(int, input().split())
n = int(input())
xyr = [tuple(map(int, input().split())) for _ in range(n)]
xyr = [(sx, sy, 0)] + xyr + [(tx, ty, 0)]

cost = [[0]*(n+2) for _ in range(n+2)]
for i, (px, py, pr) in enumerate(xyr):
    for j, (qx, qy, qr) in enumerate(xyr):
        tmp = ((px-qx) ** 2 + (py-qy) ** 2) ** 0.5 - (pr+qr)
        cost[i][j] = max(tmp, 0)

ans = dijkstra(0, n+2)
print(ans)
