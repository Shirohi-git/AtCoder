x = int(input())

dp = [0] * (x + 1)
dp[100:106] = [1] * 6
for nxt in range(200, x + 1):
    dp[nxt] = any(dp[nxt - 100 - i] for i in range(6))
print(int(dp[x]))
