n, l = map(int, input().split())
x = set(map(int, input().split()))
t = list(map(int, input().split()))
tsec = [t[0], t[0] + t[1], t[0] + 3 * t[1], t[2]]

dp = [10 ** 9] * (l + 1)
dp[0] = 0
for i in range(1, l + 1):
    dp[i] = min(dp[i - 1] + tsec[0], dp[i - 2] + tsec[1], dp[i - 4] + tsec[2])
    if i in x:
        dp[i] += tsec[3]

ans = min(dp[l], dp[l - 1] + tsec[1] // 2, dp[l - 2] + tsec[2] // 2,
          dp[l - 3] + (tsec[2] - tsec[1] // 2))
print(ans)
