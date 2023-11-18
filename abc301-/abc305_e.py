def dijkstra(n0, near0, inf=10**18):
    from heapq import heapify, heappop, heappush
    DIST = [-1] * n0
    for p, h in PH:
        DIST[p-1] = h

    que = [(-di, i) for i, di in enumerate(DIST) if di > 0]
    heapify(que)
    while que:
        d, q = heappop(que)
        if DIST[q] > -d:
            continue
        for i in near0[q]:
            tmp = -d - 1
            if DIST[i] < tmp:
                DIST[i] = tmp
                heappush(que, (-tmp, i))
    return DIST


def main():
    def nearlist(n0, lst):
        res = [[] for _ in range(n0)]
        for a, b in lst:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        return res

    near = nearlist(N, AB)
    res = dijkstra(N, near)
    ans = [i+1 for i, di in enumerate(res) if di >= 0]
    return print(len(ans)), print(*ans)


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    PH = [list(map(int, input().split())) for _ in range(K)]

    main()
