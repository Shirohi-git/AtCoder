from heapq import heappush, heappop, heapify


def prim(n0, near0):
    flag = [0] * n0
    flag[0] = 1
    que = [(c, j, 0) for j, c in near0[0]]
    heapify(que)

    res = 0
    while que:
        c_pq, q, p = heappop(que)
        if flag[q]:
            continue
        flag[q] = 1
        res += c_pq
        for r, c_qr in near0[q]:
            if 1 - flag[r]:
                heappush(que, (c_qr, r, q))
    return res if sum(flag) == N+1 else -1


def main():

    def weighted_nearlist(n0, lst0):
        res = [[] for _ in range(n0)]
        for c, a, b in lst0:
            res[a - 1].append((b, c))
            res[b].append((a - 1, c))
        return res
    
    near = weighted_nearlist(N+1, CLR)
    ans = prim(N+1, near)
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    CLR = [map(int, input().split()) for _ in range(M)]

    main()
    