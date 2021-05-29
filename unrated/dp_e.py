n, w = map(int, input().split())
item = [list(map(int, input().split())) for _ in range(n)]

VMAX = 10**5
dp = [[10**15] * (VMAX+1) for _ in range(n+1)]
dp[0][0] = 0

for i, (itw, itv) in enumerate(item):
    for j in range(VMAX+1):
        dp[i+1][j] = dp[i][j]
        if itv <= j:
            dp[i+1][j] = min(dp[i][j], dp[i][j-itv] + itw)

ans = max(i for i in range(VMAX+1) if dp[n][i] <= w)
print(ans)
