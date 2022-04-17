def main():
    dp = [0] * (N*M+1)
    dp[0] = 1

    for _ in range(1, N+1):
        nxt = [0] * (N*M+1)
        for i in range(1, M+1):
            for j in range(N*M+1):
                if i+j > N*M:
                    continue
                nxt[i+j] += dp[j]
        dp = [ni % MOD9 for ni in nxt]
    return print(sum(dp[:K+1]) % MOD9)


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    MOD9 = 998244353

    main()
