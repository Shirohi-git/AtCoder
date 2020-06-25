n, k = input(), int(input())

dp0 = [[0] * (k + 2) for _ in range(len(n) + 1)]
dp1 = [[0] * (k + 2) for _ in range(len(n) + 1)]
dp1[0][0] = 1

for i in range(len(n)):
    for j in range(k + 1):
        dp0[i + 1][j] += dp0[i][j]
        dp0[i + 1][j + 1] += dp0[i][j] * 9
        if n[i] != '0':
            dp0[i + 1][j] += dp1[i][j]
            dp0[i + 1][j + 1] += dp1[i][j] * (int(n[i]) - 1)
            dp1[i + 1][j + 1] += dp1[i][j]
        elif n[i] == '0':
            dp1[i + 1][j] += dp1[i][j]

print(dp0[len(n)][k] + dp1[len(n)][k])
