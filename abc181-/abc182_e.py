from itertools import product
import sys
input = sys.stdin.readline


def solve():
    res = 0
    for i, j in product(range(h), range(w)):
        if j - 1 >= 0:
            grid[i][j] |= grid[i][j - 1] & 2
        if i - 1 >= 0:
            grid[i][j] |= grid[i - 1][j] & 1
        if block[i][j]:
            grid[i][j] = 0
        res += (grid[i][j] > 0)
    return res


h, w, n, m = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]
cd = [tuple(map(int, input().split())) for _ in range(m)]

grid = [[0] * w for _ in range(h)]
block = [[0] * w for _ in range(h)]
for a, b in ab:
    grid[a - 1][b - 1] = 3
for c, d in cd:
    block[c - 1][d - 1] = 1
_ = solve()

grid = [gi[::-1] for gi in grid[::-1]]
block = [bi[::-1] for bi in block[::-1]]
ans = solve()
print(ans)
