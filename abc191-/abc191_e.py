from heapq import heappop, heappush


def weighted_nearlist(N):
    mat = [[-1] * N for _ in range(N)]
    for a, b, c in abc:
        if mat[a - 1][b - 1] > c or mat[a - 1][b - 1] < 0:
            mat[a - 1][b - 1] = c
    NEAR = [set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if mat[i][j] > 0:
                NEAR[i].add((j, mat[i][j]))
    return NEAR


def dijkstra(S, N):
    DIST = [-1] * N
    DIST[S] = 0

    que = [(DIST[S], S)]
    while que:
        d, q = heappop(que)
        if DIST[q] < d:
            continue
        for i, d_qi in near[q]:
            tmp = d + d_qi
            if DIST[i] > tmp or DIST[i] < 0:
                DIST[i] = tmp
                heappush(que, (tmp, i))
    return DIST


n, m = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(m)]

near = weighted_nearlist(n)
dist = [dijkstra(i, n) for i in range(n)]

for i in range(n):
    ans = -1
    for (j, c) in near[i]:
        ans += (c + 1) * (j == i)
    for j in range(n):
        s, t = dist[i][j], dist[j][i]
        if (s > 0 and t > 0) and (ans < 0 or s + t < ans):
            ans = s + t
    print(ans)
