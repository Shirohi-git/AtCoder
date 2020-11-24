import sys
sys.setrecursionlimit(10 ** 7)


def memodp(xyz):
    x, y, z = xyz
    if max(xyz) == 100:
        return 0
    if dp[x][y][z] > 0:
        return dp[x][y][z]
    res = 0
    for i, (dx, dy, dz) in zip(xyz, plus):
        if i > 0:
            nxt = (x + dx, y + dy, z + dz)
            res += i * memodp(nxt) + i
    dp[x][y][z] = res / sum(xyz)
    return dp[x][y][z]


abc = tuple(map(int, input().split()))

dp = []
for _ in range(100):
    dp.append([[0] * 100 for _ in range(100)])
plus = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
print(memodp(abc))
