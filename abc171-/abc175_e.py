r, c, k = map(int, input().split())
rcv = [map(int, input().split()) for _ in range(k)]

val = [0] * (r * c)
for ri, ci, vi in rcv:
    val[(ri - 1) * c + (ci - 1)] = vi

dp = [0] * (c + 1) * 4
for i in range(r):
    for j in range(c):
        now, v_now = 4 * j, val[i * c + j]
        dp[now] = max(dp[now - 4], max(dp[now:now + 4]))
        dp[now + 1] = max(dp[now - 3], dp[now] + v_now)
        dp[now + 2] = max(dp[now - 2], dp[now - 3] + v_now)
        dp[now + 3] = max(dp[now - 1], dp[now - 2] + v_now)
print(max(dp[-8:]))
