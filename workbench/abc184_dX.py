a, b, c = sorted(map(int, input().split()))

if b == 0:
    print(100 - c)
elif a == 0:
    dp = [[0] * 101 for _ in range(101)]
    dp[b][c] = 1
    for i in range(b, 101):
        for j in range(c, 101):
            if (i, j) == (b, c):
                continue
            if i - 1 >= b:
                dp[i][j] += dp[i - 1][j] * (i - 1) / (i + j - 1)
            if j - 1 >= c:
                dp[i][j] += dp[i][j - 1] * (j - 1) / (i + j - 1)
    print([dp[100][j] * (100 + j - b - c) for j in range(c, 100)])
    print([dp[i][100] * (100 + i - b - c) for i in range(b, 100)])
else:
    pass
