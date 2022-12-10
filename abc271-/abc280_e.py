def main():
    INV100 = pow(100, MOD9-2, MOD9)
    dp = [INF] * (N+1)
    dp[0:2] = [0, 1]
    for i in range(2, N+1):
        tmp = (dp[i-2]+1)*P + (dp[i-1]+1)*(100-P)
        dp[i] = tmp * INV100 % MOD9
    return print(dp[N])


if __name__ == '__main__':
    N, P = map(int, input().split())
    INF = 10**10
    MOD9 = 998244353

    main()
