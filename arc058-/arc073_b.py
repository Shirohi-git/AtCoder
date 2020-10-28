from itertools import product

n, w = map(int, input().split())
item = [list(map(int, input().split())) for _ in range(n)]
w1 = item[0][0]

cnt, lst = [1] * 4, [[0] for i in range(4)]
for wi, vi in sorted(item, reverse=1):
    lst[wi - w1].append(vi + lst[wi - w1][-1])
    cnt[wi - w1] += 1
r0, r1, r2, r3 = (range(ci) for ci in cnt)

ans = 0
for p in product(r0, r1, r2, r3):
    wei = sum((i + w1) * pi for i, pi in enumerate(p))
    if wei <= w:
        val = sum(lst[i][pi] for i, pi in enumerate(p))
        ans = max(ans, val)
print(ans)
