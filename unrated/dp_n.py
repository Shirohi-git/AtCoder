from itertools import accumulate

n = int(input())
a = [0] + list(accumulate(map(int, input().split())))

dp = [[0] * (n + 1) for i in range(n + 1)]

for i in range(n)[::-1]:
    for j in range(i + 1, n + 1):
        if j - i == 1:
            continue
        dp[i][j] = min([dp[i][k] + dp[k][j] for k in range(i + 1, j)])
        dp[i][j] += a[j] - a[i]

print(dp[0][n])
