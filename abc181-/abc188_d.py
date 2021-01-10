from collections import defaultdict

n, c = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(n)]

imos = defaultdict(int)
for ai, bi, ci in abc:
    imos[ai] += ci
    imos[bi + 1] -= ci

acc = [(0, 0)]
for d, sumc in sorted(imos.items()):
    acc.append((d, acc[-1][1] + sumc))

ans = 0
bfod, bfoc = acc[1]
for d, sumc in acc[2:]:
    ans += (d - bfod) * min(bfoc, c)
    bfod, bfoc = d, sumc
print(ans)
