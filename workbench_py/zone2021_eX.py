from heapq import heappop, heappush


def dijkstra(sx, sy):
    DIST = [[INF] * c for _ in range(r)]
    DIST[sx][sy] = 0

    que = [(DIST[sx][sy], sx, sy)]
    while que:
        d, p, q = heappop(que)
        if p == r and q == c:
            return DIST[r-1][c-1]
        if DIST[p][q] < d:
            continue
        for x, y, nxt in near[p*c + q]:
            tmp = d + nxt
            if DIST[x][y] > tmp:
                DIST[x][y] = tmp
                heappush(que, (tmp, x, y))
    return DIST[r-1][c-1]


r, c = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]
b = [list(map(int, input().split())) for _ in range(r-1)]
INF = 10**10

near = [[] for _ in range(c*r)]
for i in range(r):
    for j in range(c):
        if j < c-1:
            near[i*c + j].append((i, j+1, a[i][j]))
        if j > 0:
            near[i*c + j].append((i, j-1, a[i][j-1]))
        if i < r-1:
            near[i*c + j].append((i+1, j, b[i][j]))
        near[i*c + j] += [(i-k-1, j, 2+k) for k in range(i)]
ans = dijkstra(0, 0)
print(ans)
