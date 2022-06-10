from itertools import product


n = int(input())
xyh = [list(map(int, input().split())) for _ in range(n)]
xyh = sorted(xyh, key=lambda l: l[2], reverse=True)

for cx, cy in product(range(101), repeat=2):
    x0, y0, h0 = xyh[0]
    ch = h0 + abs(x0 - cx) + abs(y0 - cy)
    for x, y, h in xyh:
        if h != max(ch - abs(x - cx) - abs(y - cy), 0):
            break
    else:
        print(cx, cy, ch)
        break
