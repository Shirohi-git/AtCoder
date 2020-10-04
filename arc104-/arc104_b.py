from itertools import accumulate

n, s = input().split()
n, lst = int(n), {'A': 0, 'T': 1, 'C': 2, 'G': 3}

cnt = [[0] * (n + 1) for _ in range(4)]
for i, si in enumerate(s, 1):
    cnt[lst[si]][i] += 1
acc = [list(accumulate(c)) for c in cnt]

ans = 0
for l in range(n - 1):
    for r in range(l + 1, n + 1):
        a, t, c, g = (acc[i][r] - acc[i][l] for i in range(4))
        ans += (a == t) and (c == g)
print(ans)
