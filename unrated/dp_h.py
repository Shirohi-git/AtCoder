h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]

dp = [[0] * w for _ in range(h)]
dp[0][0] = 1

for i in range(h):
    for j in range(w):
        if (j != w - 1) and (a[i][j + 1] == '.'):
                dp[i][j + 1] += dp[i][j]
        if (i != h - 1) and (a[i + 1][j] == '.'):
                dp[i + 1][j] += dp[i][j]
print(dp[-1][-1]%(10**9+7))
