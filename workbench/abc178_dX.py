s = int(input())
mod = 10 ** 9 + 7

dp = [[0] * (s + 1) for _ in range(s // 3 + 1)]
dp[0][0] = 1
for i in range(s // 3):
    for j in range(s + 1):
        tmp = sum(dp[i][j - num] for num in range(3, min(j + 1, 10)))
        dp[i + 1][j] = tmp % mod

ans = 0
for lst in dp:
    ans = (ans + lst[s]) % mod
print(ans)
