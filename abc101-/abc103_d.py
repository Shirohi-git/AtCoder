n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
ab = sorted(ab, key=lambda x: x[1])

ans, tmp = 0, 0
for a, b in ab:
    if a >= tmp:
        tmp = b
        ans += 1
print(ans)
