from heapq import heappop, heappush


def weighted_nearlist(N):
    NEAR = [set() for _ in range(N)]
    for a, b, w in lrc:
        NEAR[a - 1].add((b - 1, w))
    return NEAR


def dijkstra(S, N):
    DIST, prev = [pow(10, 15)] * N, [-1] * N
    DIST[S], prev[S] = 0, 's'

    que = [(DIST[S], S)]
    while que:
        d, q = heappop(que)
        if DIST[q] < d:
            continue
        for i, d_qi in near[q]:
            tmp = d + d_qi
            if DIST[i] > tmp:
                DIST[i] = tmp
                prev[i] = q
                heappush(que, (tmp, i))
    return DIST


n, m = map(int, input().split())
lrc = [map(int, input().split()) for _ in range(m)]

#解説ver.
lrc += [(i + 1, i, 0) for i in range(1, n)]
near = weighted_nearlist(n)

ans = dijkstra(0, n)[-1]
print(-1 if ans == 10**15 else ans)
