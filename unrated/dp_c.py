import sys
input = sys.stdin.readline

n = int(input())
abc = [list(map(int, input().split())) for _ in range(n)]
a, b, c = 0, 1, 2

dp = [[0, 0, 0] for _ in range(n)]
dp[0] = abc[0][:]
for i in range(1, n):
    dp[i][a] = max(dp[i-1][b], dp[i-1][c]) + abc[i][a]
    dp[i][b] = max(dp[i-1][a], dp[i-1][c]) + abc[i][b]
    dp[i][c] = max(dp[i-1][b], dp[i-1][a]) + abc[i][c]

print(max(dp[n-1]))
