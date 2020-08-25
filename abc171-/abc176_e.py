H, W, m = map(int, input().split())
hw = [list(map(int, input().split())) for _ in range(m)]

row, col = [0] * H, [0] * W
for h, w in hw:
    row[h - 1] += 1
    col[w - 1] += 1

rowmax, colmax = max(row), max(col)
cnt = row.count(rowmax) * col.count(colmax)
for h, w in hw:
    if row[h - 1] == rowmax and col[w - 1] == colmax:
        cnt -= 1
print(rowmax + colmax - (cnt == 0))
