n = int(input())
dcs = [list(map(int, input().split())) for _ in range(n)]

dp = [0]*10000
for d, c, s in sorted(dcs):
    for i in range(d-c, -1, -1):
        dp[i+c] = max(dp[i+c], dp[i] + s)
print(max(dp))
