def dijkstra(s0, n0, NEAR):
    from heapq import heappop, heappush
    DIST, prev = [INF] * n0, [-1] * n0
    DIST[s0], prev[s0] = 0, 's'

    que = [(DIST[s0], s0)]
    while que:
        d, q = heappop(que)
        if DIST[q] < d:
            continue
        for i, d_qi in NEAR[q]:
            tmp = d + d_qi
            if DIST[i] > tmp:
                DIST[i] = tmp
                prev[i] = q
                heappush(que, (tmp, i))
    return prev


def main():
    def weighted_nearlist(n0):
        res = [set() for _ in range(n0)]
        for a, b, w in ABC:
            res[a - 1].add((b - 1, w))
            res[b - 1].add((a - 1, w))
        return res

    idx = {(a, b): i for i, (a, b, _) in enumerate(ABC, 1)}
    near = weighted_nearlist(N)
    bfo = dijkstra(0, N, near)
    ans = []
    for i, bi in enumerate(bfo[1:], 1):
        if i > bi:
            i, bi = bi, i
        ans.append(idx[(i+1, bi+1)])
    return print(*ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(M)]
    INF = 10**15

    main()
