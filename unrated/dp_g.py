import sys
sys.setrecursionlimit(10 ** 7)


def longdist(p, dp_l, out_l):
    if len(out_l[p]) == 0:
        return 0
    for q in out_l[p]:
        if dp_l[q] == -1:
            dp_l[q] = longdist(q, dp_l, out_l)
        dp_l[p] = max(dp_l[p], dp_l[q]+1)
    return dp_l[p]


n, m = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(m)]

input, output = [[] for _ in range(n)], [[] for _ in range(n)]
for x, y in xy:
    input[y - 1].append(x - 1)
    output[x - 1].append(y - 1)

dp = [-1] * n
for i in range(n):
    if dp[i] == -1:
        dp[i] = longdist(i, dp, output)

print(max(dp))
