from heapq import heappush, heappop, heapify
from collections import defaultdict


def prim(n0, near0, set0):
    flag = [0] * n0
    flag[0] = 1
    que = [(c, j, 0) for j, c in near0[0]]
    heapify(que)

    ans = defaultdict(int)
    while que:
        c_pq, q, p = heappop(que)
        if flag[q]:
            continue

        if (p+1, q+1, c_pq) in set0:
            ans[(p+1, q+1, c_pq)] = 1
            continue
        if (q+1, p+1, c_pq) in set0:
            ans[(q+1, p+1, c_pq)] = 1
            continue

        flag[q] = 1
        for r, c_qr in near0[q]:
            if 1 - flag[r]:
                heappush(que, (c_qr, r, q))
    return ans


def main():

    def weighted_nearlist(n0):
        res = [[] for _ in range(n0)]
        for a, b, w in ABC + UVW:
            res[a - 1].append((b - 1, w))
            res[b - 1].append((a - 1, w))
        return res

    near = weighted_nearlist(N)
    ans = prim(N, near, set(UVW))

    for uvw in UVW:
        res = ans[uvw]
        print('Yes' if res else 'No')
    return


if __name__ == '__main__':
    N, M, Q = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(M)]
    UVW = [tuple(map(int, input().split())) for _ in range(Q)]

    main()
