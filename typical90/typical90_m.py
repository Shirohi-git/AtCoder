from heapq import heappop, heappush


def weighted_nearlist(N):
    NEAR = [set() for _ in range(N)]
    for a, b, w in abc:
        NEAR[a - 1].add((b - 1, w))
        NEAR[b - 1].add((a - 1, w))
    return NEAR


def dijkstra(S, N):
    DIST = [pow(10, 10)] * N
    DIST[S] = 0

    que = [(DIST[S], S)]
    while que:
        d, q = heappop(que)
        if DIST[q] < d:
            continue
        for i, d_qi in near[q]:
            tmp = d + d_qi
            if DIST[i] > tmp:
                DIST[i] = tmp
                heappush(que, (tmp, i))
    return DIST


n, m = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(m)]

near = weighted_nearlist(n)
dist_1, dist_N = dijkstra(0, n), dijkstra(n-1, n)
for i in range(n):
    print(dist_1[i] + dist_N[i])
