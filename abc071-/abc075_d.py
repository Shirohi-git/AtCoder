from itertools import combinations

n, k = map(int, input().split())
xy = sorted(tuple(map(int, input().split())) for _ in range(n))

ans = pow(10, 20)
for l, r in combinations(range(n), 2):
    if r - l + 1 < k:
        continue
    y = sorted(yi for xi, yi in xy[l:r + 1])
    l, r = xy[l][0], xy[r][0]
    for d, u in combinations(range(len(y)), 2):
        if u - d + 1 < k:
            continue
        d, u = y[d], y[u]
        ans = min(ans, (r - l) * (u - d))
print(ans)
