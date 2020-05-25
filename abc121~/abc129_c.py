n, m = map(int, input().split())
a = set([int(input()) for _ in range(m)])
mod = 1000000007

dp = [1] + [0] * n
for i in range(1, n + 1):
    if i == 1:
        dp[i] = 1
    else:
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    if i in a:
        dp[i] = 0

print(dp[-1] % mod)
