n, m = map(int, input().split())
a = set(int(input()) for _ in range(m))
mod = 10 ** 9 + 7

dp = [1] + [1] + [0] * (n - 1)
for i in range(1, n + 1):
    if i >= 2:
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    if i in a:
        dp[i] = 0

print(dp[-1] % mod)
