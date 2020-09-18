s = int(input())
mod = 10 ** 9 + 7

dp = [1] + [0] * s
for i in range(3, s + 1):
    dp[i] = (dp[i - 1] + dp[i - 3]) % mod
print(dp[s])
