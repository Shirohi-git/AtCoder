import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def memodp(DP, x, y, LIST, MOD):
    if DP[y][x] >= 1:
        return DP[y][x]
    near = ((x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y))
    for p, q in near:
        if w > p >= 0 and h > q >= 0:
            if LIST[y][x] > LIST[q][p]:
                DP[y][x] += memodp(DP, p, q, LIST, MOD)
    DP[y][x] = (DP[y][x] + 1) % MOD
    return DP[y][x]

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
mod = 10 ** 9 + 7

dp = [[0] * w for _ in range(h)]
for i in range(w):
    for j in range(h):
        memodp(dp, i, j, a, mod)

print(sum(sum(l) % mod for l in dp) % mod)
