from itertools import product

a, b, c, d, e, f = map(int, input().split())

lima = [100 * a * i for i in range(f // (100 * a) + 1)]
limb = [100 * b * i for i in range(f // (100 * b) + 1)]
setw = set([i + j for i, j in product(lima, limb) if 0 < i + j <= f])
limc = [c * i for i in range(f // c + 1)]
limd = [d * i for i in range(f // d + 1)]
sets = set([i + j for i, j in product(limc, limd) if 0 < i + j <= f])

cnt, ans = 0, (max(setw), 0)
for w in setw:
    for s in sets:
        if (cnt <= 100 * s / w <= e) and (s + w <= f):
            cnt = 100 * s / w
            ans = s + w, s
else:
    print(*ans)
