n, k = map(int, input().split())
a = list(map(int, input().split()))

cs_a, cnt = [0] * n, 0
for i in range(n):
    cnt += a[i]
    cs_a[i] = cnt
dp = [[0] * (k + 1) for i in range(n + 1)]

for i in range(n + 1):
    for j in range(k + 1):
        if j == 0:
            dp[i][j] = 1
        elif (i == 0) or (j > cs_a[i - 1]):
            dp[i][j] = 0
        elif j == 1:
            dp[i][j] = dp[i - 1][j] + min(a[i - 1], 1)
        elif j - a[i - 1] - 1 < 0:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - \
                dp[i - 1][j - a[i - 1] - 1]
        dp[i][j] %= 10 ** 9 + 7

print(dp[n][k])
