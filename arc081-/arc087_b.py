from collections import defaultdict

s = input() + 'T'
x, y = map(int, input().split())

scnt = []
cnt = 0
for si in s:
    if si == 'T':
        scnt.append(cnt)
        cnt = 0
    cnt += (si == 'F')

ini, (ldiv, lmod) = len(s) + 1, divmod(len(scnt) + 2, 2)
xdp = [defaultdict(int) for _ in range(ldiv + lmod)]
ydp = [defaultdict(int) for _ in range(ldiv)]

xdp[1][ini + scnt[0]], ydp[0][ini] = 1, 1
for i, d in enumerate(scnt[1:], 1):
    div, mod = divmod(i + 2, 2)
    lst = ydp[div] if mod else xdp[div]
    bfo = ydp[div - 1] if mod else xdp[div - 1]
    for b in bfo.keys():
        lst[b + d] = 1
        lst[b - d] = 1
res = xdp[-1][x + ini] & ydp[-1][y + ini]
print('Yes' if res else 'No')
