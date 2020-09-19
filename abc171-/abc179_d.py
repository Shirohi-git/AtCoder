n, k = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(k)]
mod = 998244353

# 解説AC
dp, acc = [0] * (n + 1), [0] * (n + 1)
dp[1], acc[1] = 1, 1
for i in range(2, n + 1):
    for l, r in lr:
        accl, accr = max(i - (r + 1), 0), max(i - l, 0)
        dp[i] += acc[accr] - acc[accl]
    dp[i] %= mod
    acc[i] = (dp[i] + acc[i - 1]) % mod
print(dp[n])
