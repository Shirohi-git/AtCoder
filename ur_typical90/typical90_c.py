def nearlist(N):
    NEAR = [set() for _ in range(N)]
    for a, b in ab:
        NEAR[a - 1].add(b - 1)
        NEAR[b - 1].add(a - 1)
    return NEAR


def bfs(S, N):
    dist = [-1] * N
    dist[S] = 0
    que = [S]

    for q in que:
        for i in near[q]:
            if dist[i] > -1:
                continue
            dist[i] = dist[q] + 1
            que.append(i)
    return q, dist[q]


n = int(input())
ab = [list(map(int, input().split())) for _ in range(n-1)]

near = nearlist(n)
u, _ = bfs(0, n)
v, long = bfs(u, n)
print(long + 1)
