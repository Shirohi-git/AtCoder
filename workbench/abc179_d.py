n, k = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(k)]
mod = 998244353

s = []
for l, r in lr:
    s += [i for i in range(l, r + 1)]

dp = [0] * (n + 1)
dp[1] = 1
for i in range(2, n + 1):
    for j in s:
        dp[i] += dp[max(i - j, 0)]
    dp[i] %= mod
print(dp[n])
