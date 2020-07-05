from itertools import product
from copy import deepcopy

h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]

ans = 0
for hl in product([0, 1], repeat=h):
    for wl in product([0, 1], repeat=w):
        cc = deepcopy(c)
        for i, hi in enumerate(hl):
            for j, wj in enumerate(wl):
                if hi == 1 or wj == 1:
                    cc[i][j] = 'r'
        cnt = 0
        for s in cc:
            cnt += sum(si == '#' for si in s)
        if cnt == k:
            ans += 1
print(ans)
