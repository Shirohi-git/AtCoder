h, w = map(int, input().split())
s = [input() for _ in range(h)]
MOD = 10 ** 9 + 7

dp = [[0] * w for _ in range(h)]
acch = [0 for _ in range(w)]
accw = [0 for _ in range(h)]
accd = [0 for _ in range(h + w)]
dp[0][0] = 1

for i in range(h):
    for j in range(w):
        d = h - (i - j)
        if s[i][j] == '.':
            plus = accw[i] + acch[j] + accd[d]
            dp[i][j] = (dp[i][j] + plus) % MOD
            accw[i] = (accw[i] + dp[i][j]) % MOD
            acch[j] = (acch[j] + dp[i][j]) % MOD
            accd[d] = (accd[d] + dp[i][j]) % MOD
        if s[i][j] == '#':
            dp[i][j] = 0
            accw[i], acch[j], accd[d] = 0, 0, 0
print(dp[-1][-1])
