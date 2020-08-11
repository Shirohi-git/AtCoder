s = input()
mod = 10 ** 9 + 7

dp = [[0] * 13 for i in range(len(s))]
if s[0] == '?':
    dp[0] = [1] * 10 + [0] * 3
else:
    dp[0] = [int(i == int(s[0])) for i in range(13)]

for i, si in enumerate(s[1:], 1):
    for j in range(13):
        if si == '?':
            for k in range(10):
                dp[i][(10 * j + k) % 13] += dp[i - 1][j]
                dp[i][(10 * j + k) % 13] %= mod
        else:
            dp[i][(10 * j + int(si)) % 13] += dp[i - 1][j]
            dp[i][(10 * j + int(si)) % 13] %= mod
print(dp[-1][5] % mod)
