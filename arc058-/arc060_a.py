from collections import defaultdict

n, a = map(int, input().split())
x = list(map(int, input().split()))
y = [xi - a for xi in x]

# 解説AC
dp = [defaultdict(int) for i in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in dp[i]:
        dp[i + 1][j + y[i]] += dp[i][j]
        dp[i + 1][j] += dp[i][j]
print(dp[n][0] - 1)
