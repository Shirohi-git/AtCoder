from heapq import heappop, heappush


def nearlist(N):
    NEAR = [[] for _ in range(N)]
    for a, b, t, k in abtk:
        NEAR[a - 1].append([b - 1, t, k])
        NEAR[b - 1].append([a - 1, t, k])
    return NEAR


def dijkstra(S, G):
    time = [10 ** 15] * n
    time[S] = 0

    que = [(time[S], S)]
    while que:
        d, q = heappop(que)
        if time[q] < d:
            continue
        for i, t, k in near[q]:
            tmp = (d + k - 1) // k * k + t
            if time[i] > tmp:
                time[i] = tmp
                heappush(que, (tmp, i))
    return -1 if time[G] == 10 ** 15 else time[G]


n, m, x, y = map(int, input().split())
abtk = [list(map(int, input().split())) for _ in range(m)]

near = nearlist(n)
print(dijkstra(x - 1, y - 1))
