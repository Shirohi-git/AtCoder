h, w = map(int, input().split())
s = [input() for _ in range(h)]
MOD = 10 ** 9 + 7

dpl = [[1] * w for _ in range(h)]
dpr = [[1] * w for _ in range(h)]
dpu = [[1] * w for _ in range(h)]
dpd = [[1] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if j - 1 >= 0:
            dpl[i][j] += dpl[i][j - 1]
        if i - 1 >= 0:
            dpu[i][j] += dpu[i - 1][j]
        if s[i][j] == '#':
            dpl[i][j], dpu[i][j] = 0, 0
for i in range(h)[::-1]:
    for j in range(w)[::-1]:
        if j + 1 < w:
            dpr[i][j] += dpr[i][j + 1]
        if i + 1 < h:
            dpd[i][j] += dpd[i + 1][j]
        if s[i][j] == '#':
            dpr[i][j], dpd[i][j] = 0, 0

K = sum(si.count('.') for si in s)
pow2 = [1]
for i in range(K + 3):
    pow2.append((pow2[-1] * 2) % MOD)

ans = K * pow2[K] % MOD
for i in range(h):
    for j in range(w):
        cnt = (dpl[i][j] + dpu[i][j]
               + dpr[i][j] + dpd[i][j] - 3)
        ans -= pow2[K - cnt] * (s[i][j] == '.')
print(ans % MOD)
