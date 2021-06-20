def main():
    dp = [0] * (N+L+1)
    dp[0] = 1
    for i in range(N+1):
        dp[i] -= MOD1 * (dp[i] >= MOD1)
        dp[i+1] += dp[i]
        dp[i+L] += dp[i]
    return print(dp[N])


if __name__ == '__main__':
    N, L = map(int, input().split())
    MOD1 = 10**9 + 7

    main()
