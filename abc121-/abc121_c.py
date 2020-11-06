n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

ans, cnt = 0, 0
for a, b in sorted(ab):
    if cnt < m:
        ans += a * min(b, m - cnt)
        cnt += min(b, m - cnt)
print(ans)
