h, n = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

dp = [float('inf')] * (h + 1)
dp[0] = 0

for i in range(h + 1):
    for a, b in ab:
        dp[i] = min(dp[i], dp[max(i - a, 0)] + b)
print(dp[h])
