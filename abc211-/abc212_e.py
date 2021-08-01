def main():
    dp = [0] * N
    dp[0] = 1
    for _ in range(K):
        sum_dp = sum(dp) % MOD9
        nxt = [sum_dp] * N
        for u, v in UV:
            nxt[u-1] -= dp[v-1]
            nxt[v-1] -= dp[u-1]
        for i in range(N):
            nxt[i] -= dp[i]
            nxt[i] %= MOD9
        dp = nxt[:]
    return print(dp[0])


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    UV = [list(map(int, input().split())) for _ in range(M)]
    MOD9 = 998244353

    main()
