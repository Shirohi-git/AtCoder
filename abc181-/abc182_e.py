from itertools import product
import sys
input = sys.stdin.readline


def solve():
    res = 0
    for i, j in product(range(1, h + 1), range(1, w + 1)):
        grid[i][j] |= grid[i][j - 1] & 2
        grid[i][j] |= grid[i - 1][j] & 1
        grid[i][j] = min(grid[i][j], 4)
        res += (0 < grid[i][j] < 4)
    return res


h, w, n, m = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]
cd = [tuple(map(int, input().split())) for _ in range(m)]

grid = [[0] * (w + 2) for _ in range(h + 2)]
for a, b in ab:
    grid[a][b] = 3
for c, d in cd:
    grid[c][d] = 4
solve()

grid = [gi[::-1] for gi in grid[::-1]]
print(solve())
