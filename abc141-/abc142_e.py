import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ac = []
for i in range(m):
    a, b = map(int, input().split())
    tmpc = map(int, input().split())
    c = sum(1 << (ci - 1) for ci in tmpc)
    ac.append((a, c))

# 解説AC
dp = [[0] + [pow(10, 9)] * (pow(2, n) - 1)]
for i, (ai, ci) in enumerate(ac, 1):
    dp.append(dp[-1][:])
    for j in range(pow(2, n)):
        tmp = min(dp[i - 1][j | ci], dp[i - 1][j] + ai)
        dp[i][j | ci] = min(tmp, dp[i][j | ci])
print(-1 if dp[-1][-1] == pow(10, 9) else dp[-1][-1])
