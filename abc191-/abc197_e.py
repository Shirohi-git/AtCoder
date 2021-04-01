n = int(input())
xc = [list(map(int, input().split())) for _ in range(n)]

ball = [[] for _ in range(n + 2)]
for x, c in xc:
    ball[c].append(x)
ball[0], ball[-1] = [0], [0]

dp = [[float('inf')] * 2 for _ in range(n + 2)]
dp[0] = [0, 0]
bfo, blst = 0, ball[0]
for i, lst in enumerate(ball):
    if lst:
        lst = sorted(lst)
        for j in [0, 1]:
            dp[i][j] = min(dp[bfo][0] + abs(blst[0] - lst[j - 1]),
                           dp[bfo][1] + abs(blst[-1] - lst[j - 1]))
            dp[i][j] += abs(lst[0] - lst[-1])
        bfo, blst = i, [lst[0], lst[-1]]
print(min(dp[-1]))
