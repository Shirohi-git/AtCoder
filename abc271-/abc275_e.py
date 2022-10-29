def main():
    minv = pow(M, MOD9-2, MOD9)

    ans = 0
    dp = [1] + [0] * N
    for _ in range(K):
        nxt = [0] * (N+1)
        for i in range(N):
            for j in range(1,M+1):
                if i+j > N:
                    nxt[N-(i+j-N)] += dp[i] * minv
                else:
                    nxt[i+j] += dp[i] * minv
        dp = [ni % MOD9 for ni in nxt]
        ans += dp[-1]
    return print(ans % MOD9)


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    MOD9 = 998244353

    main()
