from collections import defaultdict
from itertools import permutations

n, c = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(c)]
cmat = [list(map(int, input().split())) for _ in range(n)]

dcnt = [defaultdict(int) for _ in range(3)]
for i, ci in enumerate(cmat):
    for j, cij in enumerate(ci):
        mod = (i + j) % 3
        dcnt[mod][cij - 1] += 1

ans = 10 ** 9
for color in permutations(range(c), 3):
    tmp = 0
    for tgt, cnt in zip(color, dcnt):
        tmp += sum(d[k][tgt] * cnt[k] for k in cnt)
    ans = min(ans, tmp)
print(ans)
