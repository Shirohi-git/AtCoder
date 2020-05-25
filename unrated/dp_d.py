import sys
input = sys.stdin.readline

n, w = map(int, input().split())
item = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] + [0]*w] + [[-float("inf")]*(w+1) for _ in range(n)]
wei, val = 0, 1

for i in range(n):
    for j in range(w+1):
        if item[i][wei] <= j:
            dp[i+1][j] = max(dp[i][j], dp[i][j-item[i][wei]] + item[i][val])
        else:
            dp[i+1][j] = dp[i][j]

print(dp[n][w])
