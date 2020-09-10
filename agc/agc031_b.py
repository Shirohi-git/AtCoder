n = int(input())
c = [int(input()) for _ in range(n)]
mod = 10 ** 9 + 7

# 解説AC
dp = [1] * n
color = [-1] * max(c)
for i, ci in enumerate(c):
    dp[i] = dp[i - 1]
    if 0 <= color[ci - 1] < i - 1:
        dp[i] += dp[color[ci - 1]]
        dp[i] %= mod
    color[ci - 1] = i
print(dp[-1])
