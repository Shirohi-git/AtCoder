def prim(n0, near0):
    from heapq import heappush, heappop, heapify

    flag = [0] * n0
    flag[0] = 1
    que = [(c, j, 0) for j, c in near0[0]]
    heapify(que)

    res = set((min(a, b), max(a, b), c) for a, b, c in ABC)
    while que:
        c_pq, q, p = heappop(que)
        if flag[q]:
            continue
        flag[q] = 1
        res.remove((min(p, q)+1, max(p, q)+1, c_pq))
        for r, c_qr in near0[q]:
            if 1 - flag[r]:
                heappush(que, (c_qr, r, q))
    return res


def main():

    def nearlist():
        NEAR = [set() for _ in range(N)]
        for a, b, c in ABC:
            NEAR[a - 1].add((b - 1, c))
            NEAR[b - 1].add((a - 1, c))
        return NEAR

    near = nearlist()
    ans = sum(ci for _, _, ci in prim(N, near) if ci > 0)
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(M)]

    main()
