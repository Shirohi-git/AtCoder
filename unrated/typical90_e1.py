def main():
    n, b, k = map(int, input().split())
    c = list(map(int, input().split()))

    if n > 1e4:
        exit()

    # 小課題1 O(nb)
    dp = [[0] * b for _ in range(n+1)]
    for ci in c:
        dp[1][ci % b] += 1

    for i in range(1, n):
        for j in range(b):
            for ck in c:
                nxt = (j*10 + ck) % b
                dp[i+1][nxt] += dp[i][j]
                dp[i+1][nxt] %= MOD1
    print(dp[n][0])

if __name__ == '__main__':
    MOD1 = 10**9 + 7
    main()
