h, w, k = map(int, input().split())
MOD = 10 ** 9 + 7

dp = [[0] * w for _ in range(h + 1)]
dp[0][0] = 1

# tmpの前計算をしろ
tmp = 1
for i in range(h):
    for j in range(w):
        dp[i + 1][j] += dp[i][j] * tmp
        dp[i + 1][j] %= MOD

        if j - 1 >= 0:
            dp[i + 1][j - 1] += dp[i][j] * tmp
            dp[i + 1][j - 1] %= MOD
        if j + 1 < w:
            dp[i + 1][j + 1] += dp[i][j] * tmp
            dp[i + 1][j + 1] %= MOD

print(dp[h][k - 1])
