n, x = map(int, input().split())
vp = [list(map(int, input().split())) for _ in range(n)]

y = 0
for i, (v, p) in enumerate(vp):
    y += v * p
    if y > x * 100:
        exit(print(i + 1))
print(-1)
