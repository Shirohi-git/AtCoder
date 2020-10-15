from itertools import product

h, w, k = map(int, input().split())
MOD = 10 ** 9 + 7

cnt = [[0, 0, 0] for _ in range(w)]
for l in product([0, 1], repeat=w - 1):
    l += (0,)
    if any(l[i] + l[i + 1] > 1 for i in range(w - 2)):
        continue
    for i in range(w):
        cnt[i][(1 - l[i - 1]) + l[i]] += 1

dp = [[0] * (w + 1) for _ in range(h + 1)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        dp[i + 1][j - 1] += dp[i][j] * cnt[j][0]
        dp[i + 1][j] += dp[i][j] * cnt[j][1]
        dp[i + 1][j + 1] += dp[i][j] * cnt[j][2]
    dp[i + 1] = [num % MOD for num in dp[i + 1]]
print(dp[h][k - 1])
