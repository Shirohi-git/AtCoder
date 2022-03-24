def main():
    def nearlist(N, LIST):
        res = [[] for _ in range(N)]
        for a, b in LIST:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        return res

    near = nearlist(N, UV)
    dp_0, dp_1 = [0] * N, [0] * N
    dp_0[S-1] = 1
    for _ in range(K):
        nxt_0, nxt_1 = [0] * N, [0] * N
        for i in range(N):
            for j in near[i]:
                if j == X-1:
                    nxt_0[j] += dp_1[i]
                    nxt_1[j] += dp_0[i]
                elif j != X-1:
                    nxt_0[j] += dp_0[i]
                    nxt_1[j] += dp_1[i]
        dp_0 = [n0 % MOD9 for n0 in nxt_0]
        dp_1 = [n1 % MOD9 for n1 in nxt_1]
    return print(dp_0[T-1])


if __name__ == '__main__':
    N, M, K, S, T, X = map(int, input().split())
    UV = [list(map(int, input().split())) for _ in range(M)]
    MOD9 = 998244353

    main()
