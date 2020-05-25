import sys
input = sys.stdin.readline

n, w = map(int, input().split())
v = 100*10**3
item = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] + [float("inf")]*v] + [[float("inf")]*(v+1) for _ in range(n)]
wei, val = 0, 1

for i in range(n):
    for j in range(v+1):
        if item[i][val] <= j:
            dp[i+1][j] = min(dp[i][j], dp[i][j-item[i][val]]+item[i][wei])
            # 価値j以下のもとで重さ最小化
        else:
            dp[i+1][j] = dp[i][j]

for i in range(v+1):
    if (dp[n][i] <= w):
        ans = i
print(ans)
