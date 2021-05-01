from heapq import heappop, heappush


def weighted_nearlist(N):
    NEAR = [set() for _ in range(N)]
    for a, b, w in abc:
        NEAR[a - 1].add((b - 1, w))
        NEAR[b - 1].add((a - 1, w))
        cnt[a-1][b-1], cnt[b-1][a-1] = 1, 1
    return NEAR


def dijkstra(S, N):
    DIST, prev = [10**6] * N, [-1] * N
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

    for now, bfo in enumerate(prev):
        if bfo == 's':
            continue
        cnt[now][bfo], cnt[bfo][now] = 0, 0
    return 0


n, m = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(m)]

cnt = [[0] * n for _ in range(n)]
near = weighted_nearlist(n)
for i in range(n):
    dijkstra(i, n)
ans = sum(sum(cnt[i]) for i in range(n))
print(ans // 2)
