from math import pi
from itertools import accumulate

n, q = map(int, input().split())
xrh = [list(map(int, input().split())) for _ in range(n)]
ab = [list(map(int, input().split())) for _ in range(q)]

v = [0 for _  in range(10 ** 5)]
for x, r, h in xrh:
    btm = r
    for j in range(h):
        top = ((h - (j + 1)) * r) / h
        v[x + j] += pi * (btm ** 2 + btm * top + top ** 2) / 3
        btm = top

sumv = [0] + list(accumulate(v))
for a, b in ab:
    print(sumv[b] - sumv[a])
