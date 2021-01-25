def nearlist(N):
    NEAR = [set() for _ in range(N)]
    for a, b in xy:
        NEAR[a - 1].add(b - 1)
    return NEAR

n, m = map(int, input().split())
a = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(m)]

dp = [10 ** 10] * n
near = nearlist(n)
for i in range(n):
    for j in near[i]:
        dp[j] = min(a[i], dp[i], dp[j])

ans = max(ai - dpi for dpi, ai in zip(dp, a))
print(ans)
