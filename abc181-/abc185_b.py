n, m, t = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)] + [[t, t]]

cnt, res, time = n, True, 0
for a, b in ab:
    cnt -= a - time
    if cnt <= 0:
        res = False
    cnt, time = min(cnt + b - a, n), b
print('Yes' if res else 'No')
