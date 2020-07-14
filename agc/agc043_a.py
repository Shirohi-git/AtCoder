h, w = map(int, input().split())
s = [input() for _ in range(h)]

dp = [[h * w] * w for _ in range(h)]
dp[0][0] = int(s[0][0] == '#')
for i in range(h):
    for j in range(w):
        if i + 1 < h:
            dp[i + 1][j] = min(dp[i + 1][j],
                               dp[i][j] + int(s[i + 1][j] != s[i][j]))
        if j + 1 < w:
            dp[i][j + 1] = min(dp[i][j + 1],
                               dp[i][j] + int(s[i][j + 1] != s[i][j]))
print((dp[-1][-1] + 1) // 2)
