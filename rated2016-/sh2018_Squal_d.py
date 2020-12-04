from heapq import heappop, heappush, heapify


def nearlist():
    NEAR = [set() for _ in range(n)]
    for x, y, a, b in uvab:
        NEAR[x - 1].add((y - 1, a, b))
        NEAR[y - 1].add((x - 1, a, b))
    return NEAR


def dijkstra(S, KEY):
    DIST = [upper] * n
    DIST[S] = 0

    que = [(DIST[S], S)]
    while que:
        d, q = heappop(que)
        for i, *d_qi in near[q]:
            tmp = d + d_qi[KEY]
            if DIST[i] > tmp:
                DIST[i] = tmp
                heappush(que, (tmp, i))
    return DIST


n, m, s, t = map(int, input().split())
uvab = [list(map(int, input().split())) for _ in range(m)]
upper = 10 ** 15

near = nearlist()
dist_a, dist_b = dijkstra(s - 1, 0), dijkstra(t - 1, 1)
cost = [(da + db, i) for i, da, db in zip(range(n), dist_a, dist_b)]
heapify(cost)

c, v = 0, -1
for i in range(n):
    while v < i:
        c, v = heappop(cost)
    print(upper - c)
