a, b, c, d = map(int, input().split())
MOD9 = 998244353

dp = [[0] * (d + 1) for _ in range(c + 1)]
dp[a][b] = 1

for i in range(c + 1):
    for j in range(d + 1):
        if i - 1 >= 0:
            dp[i][j] += dp[i - 1][j] * j
        if j - 1 >= 0:
            dp[i][j] += dp[i][j - 1] * i
        if i - 1 >= 0 and j - 1 >= 0:
            cmb = (i - 1) * (j - 1)
            dp[i][j] -= dp[i - 1][j - 1] * cmb
        dp[i][j] %= MOD9
print(dp[-1][-1])
