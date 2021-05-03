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

        if q > 0 and d + A[p][q-1] < DIST[p][q-1]:
            heappush(que, (d + A[p][q-1], p, q-1))
            DIST[p][q-1] = d + A[p][q-1]
        if q < c-1 and d + A[p][q] < DIST[p][q+1]:
            heappush(que, (d + A[p][q], p, q+1))
            DIST[p][q+1] = d + A[p][q]
        if p < r-1 and d + B[p][q] < DIST[p+1][q]:
            heappush(que, (d + B[p][q], p+1, q))
            DIST[p+1][q] = d + B[p][q]
        for i in range(1, p+1):
            if d + 1+i < DIST[p-i][q]:
                heappush(que, (d + 1+i, p-i, q))
                DIST[p-i][q] = d + 1+i
    return DIST[r-1][c-1]


r, c = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(r)]
B = [list(map(int, input().split())) for _ in range(r-1)]
INF = 10**10

# O(n**3*logn)
ans = dijkstra(0, 0)
print(ans)
