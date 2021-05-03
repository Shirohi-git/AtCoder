from heapq import heappop, heappush


def dijkstra(xy):
    DIST = [INF] * (c*r * 2)
    DIST[0] = 0

    que = [(DIST[0], 0)]
    while que:
        d, p = heappop(que)
        if p == c*r - 1:
            return DIST[c*r - 1]
        if DIST[p] < d:
            continue
        for nxt, nxt_d in near[p]:
            tmp = d + nxt_d
            if DIST[nxt] > tmp:
                DIST[nxt] = tmp
                heappush(que, (tmp, nxt))
    return DIST[-1][-1]

# 解説AC O(rclog(rc))
r, c = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]
b = [list(map(int, input().split())) for _ in range(r-1)]
INF = 10**10

near = [[] for _ in range(c*r * 2)]
for i in range(r):
    for j in range(c):
        v1 = i*c + j
        if j < c-1:
            near[v1].append((v1+1, a[i][j]))
        if j > 0:
            near[v1].append((v1-1, a[i][j-1]))
        if i < r-1:
            near[v1].append((v1+c, b[i][j]))
        v2 = v1 + c*r
        near[v1].append((v2, 1))
        near[v2].append((v1, 0))
        if i > 0:
            near[v2].append((v2-c, 1))

ans = dijkstra(0)
print(ans)
