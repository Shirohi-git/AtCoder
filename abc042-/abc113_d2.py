h, w, k = map(int, input().split())
MOD = 10 ** 9 + 7

# 解説fibo ver.
fibo = [1, 1]
for _ in range(3, w + 1):
    fibo.append(sum(fibo[-2:]))
fibo += [0, ]

dp = [[0] * (w + 1) for _ in range(h + 1)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        dp[i + 1][j - 1] += dp[i][j] * fibo[j - 1] * fibo[w - j - 1]
        dp[i + 1][j] += dp[i][j] * fibo[j] * fibo[w - j - 1]
        dp[i + 1][j + 1] += dp[i][j] * fibo[j] * fibo[w - j - 2]
    dp[i + 1] = [num % MOD for num in dp[i + 1]]
print(dp[h][k - 1])
