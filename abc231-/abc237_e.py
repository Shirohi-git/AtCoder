def main():
    def weighted_nearlist(n0):
        res = [[] for _ in range(n0)]
        for a, b in UV:
            ha, hb = H[a - 1], H[b - 1]
            if ha < hb:
                a, b = b, a
                ha, hb = hb, ha
            res[a - 1].append((b - 1, 0))
            res[b - 1].append((a - 1, ha - hb))
        return res

    def dijkstra(s0, n0):
        from heapq import heappop, heappush
        DIST = [pow(10, 10)] * n0
        DIST[s0] = 0

        que = [(DIST[s0], s0)]
        while que:
            d, q = heappop(que)
            if DIST[q] < d:
                continue
            for i, d_qi in near[q]:
                tmp = d + d_qi
                if DIST[i] > tmp:
                    DIST[i] = tmp
                    heappush(que, (tmp, i))
        return DIST

    near = weighted_nearlist(N)
    ans = dijkstra(0, N)
    return print(max(-ai - hi for ai, hi in zip(ans, H)) + H[0])


if __name__ == '__main__':
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    UV = [list(map(int, input().split())) for _ in range(M)]

    main()
