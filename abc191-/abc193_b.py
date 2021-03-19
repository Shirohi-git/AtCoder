n = int(input())
apx = [list(map(int, input().split())) for _ in range(n)]

ans = -1
for a, p, x in apx:
    if x - a > 0:
        ans = (p if ans < 0 else min(ans, p))
print(ans)
