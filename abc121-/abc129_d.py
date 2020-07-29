h, w = map(int, input().split())
s = [input() for _ in range(h)]

dpl = [[1] * w for _ in range(h)]
dpr = [[1] * w for _ in range(h)]
dpu = [[1] * w for _ in range(h)]
dpd = [[1] * w for _ in range(h)]

for i, si in enumerate(s):
    for j, sij in enumerate(si):
        if sij == '#':
            dpl[i][j], dpu[i][j] = 0, 0
        elif sij == '.':
            if j - 1 >= 0:
                dpl[i][j] = dpl[i][j - 1] + 1
            if i - 1 >= 0:
                dpu[i][j] = dpu[i - 1][j] + 1
for i, si in enumerate(s[::-1]):
    i = h - i - 1
    for j, sij in enumerate(si[::-1]):
        j = w - j - 1
        if sij == '#':
            dpr[i][j], dpd[i][j] = 0, 0
        elif sij == '.':
            if j + 1 < w:
                dpr[i][j] = dpr[i][j + 1] + 1
            if i + 1 < h:
                dpd[i][j] = dpd[i + 1][j] + 1

ans = 0
for i in range(h):
    for j in range(w):
        cnt = dpl[i][j] + dpr[i][j] + dpu[i][j] + dpd[i][j]
        ans = max(ans, cnt)
print(ans - 3)
