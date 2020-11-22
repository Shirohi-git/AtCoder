n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]

for a, b in ab:
    res, dist = -1, 10 ** 10
    for i, (c, d) in enumerate(cd, 1):
        tmp = abs(a - c) + abs(b - d)
        if tmp < dist:
            res, dist = i, tmp
    print(res)
