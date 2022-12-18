def prim(n0, near0):
    from heapq import heappush, heappop, heapify

    flag = [0] * n0
    flag[0] = 1
    que = [(c, j, 0) for j, c in near0[0]]
    heapify(que)

    ans = 0
    while que:
        c_pq, q, p = heappop(que)
        if flag[q]:
            continue
        flag[q] = 1
        ans += c_pq
        for r, c_qr in near0[q]:
            if 1 - flag[r]:
                heappush(que, (c_qr, r, q))
    return ans


def main():
    near = [[] for _ in range(N)]
    for i, ai in enumerate(A):
        for j, aj in enumerate(A[:i]):
            w = (pow(ai, aj, M) + pow(aj, ai, M)) % M
            near[i].append((j, -w))
            near[j].append((i, -w))
    ans = prim(N, near)
    return print(-ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    main()
