def main():
    dp = [1] * 11
    for _ in range(N-1):
        nxt = [0] * 11
        for j in range(1, 10):
            nxt[j-1] += dp[j]
            nxt[j] += dp[j]
            nxt[j+1] += dp[j]
        dp = list(map(lambda x: x % MOD9, nxt))
    return print(sum(dp[1:10]) % MOD9)


if __name__ == '__main__':
    N = int(input())
    MOD9 = 998244353

    main()
