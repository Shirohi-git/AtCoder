w, h, n = map(int, input().split())
xya = [list(map(int, input().split())) for _ in range(n)]

l, r, b, t = 0, w, 0, h
for x, y, a in xya:
    if a == 1:
        l = max(x, l)
    elif a == 2:
        r = min(x, r)
    elif a == 3:
        b = max(y, b)
    elif a == 4:
        t = min(y, t)
print(max(0, r - l) * max(0, t - b))
