def main():
    
    def make_dist():
        res, bc = [0] * POW2N, [0] * POW2N
        for bit in range(POW2N):
            lst = [i for i in range(N) if (bit >> i) & 1]
            bc[bit] = len(lst)
            for i in lst:
                for j in lst:
                    (xi, yi), (xj, yj) = XY[i], XY[j]
                    dist = (xi-xj)**2 + (yi-yj)**2
                    res[bit] = max(res[bit], dist)
        return res, bc

    def make_subset():
        res = [[0]]
        for i in range(N):
            pow2i = 1 << i
            nxt = []
            for ri in res:
                nxt.append(ri[:] + [pow2i + rij for rij in ri])
            res += nxt
        return res

    (max_d, bitcnt), subset = make_dist(), make_subset()

    dp = [[INF] * POW2N for _ in range(K)]
    dp[0] = max_d[:]
    for cnt in range(1, K):
        for bit in range(POW2N):
            if bitcnt[bit] <= cnt:
                continue
            tmp = INF
            for sub in subset[bit]:
                tmp = min(tmp, max(max_d[bit-sub], dp[cnt-1][sub]))
            dp[cnt][bit] = tmp
    return print(dp[-1][-1])


if __name__ == '__main__':
    N, K = map(int, input().split())
    XY = [tuple(map(int, input().split())) for _ in range(N)]
    INF, POW2N = 3 * 10**18, 1 << N

    main()
