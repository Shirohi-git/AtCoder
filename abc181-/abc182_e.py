import sys
input = sys.stdin.readline

h, w, n, m = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]
cd = [tuple(map(int, input().split())) for _ in range(m)]

grid = [[0] * w for _ in range(h)]
block = [[0] * w for _ in range(h)]
for a, b in ab:
    grid[a - 1][b - 1] = 3
for c, d in cd:
    block[c - 1][d - 1] = 1

for i in range(h):
    for j in range(w):
        if j - 1 >= 0:
            grid[i][j] |= grid[i][j - 1] & 2
        if i - 1 >= 0:
            grid[i][j] |= grid[i - 1][j] & 1
        if block[i][j]:
            grid[i][j] = 0
for i in range(h)[::-1]:
    for j in range(w)[::-1]:
        if j + 1 < w:
            grid[i][j] |= grid[i][j + 1] & 2
        if i + 1 < h:
            grid[i][j] |= grid[i + 1][j] & 1
        if block[i][j]:
            grid[i][j] = 0

ans = sum(sum(gij > 0 for gij in gi) for gi in grid)
print(ans)
