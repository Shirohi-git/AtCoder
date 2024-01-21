def main():
    dp = [1] + [0] * (INF-1)
    for t, x in Query:
        x = int(x)
        if t == '+':
            for i in range(INF)[::-1]:
                if i-x >= 0:
                    dp[i] += dp[i-x]
        else:  # elif t == '-':
            for i in range(INF):
                if i-x >= 0:
                    dp[i] -= dp[i-x]
        dp = [di % MOD9 for di in dp]
        print(dp[K])
    return


if __name__ == '__main__':
    Q, K = map(int, input().split())
    Query = [input().split() for _ in range(Q)]
    
    INF = 5001
    MOD9 = 998244353

    main()

