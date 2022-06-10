from copy import deepcopy
from itertools import permutations


def warshallfloyd(N):  # ワーシャルフロイド法:全頂点対最短経路 O(n**3)
    DIST = deepcopy(mat)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                DIST[i][j] = min(DIST[i][j], DIST[i][k] + DIST[k][j])
    return DIST


n, m, r = map(int, input().split())
town = list(map(int, input().split()))
abc = [list(map(int, input().split())) for _ in range(m)]

mat = [[10 ** 10] * n for _ in range(n)]
for i in range(n):
    mat[i][i] = 0
for a, b, c in abc:
    mat[a - 1][b - 1] = c
    mat[b - 1][a - 1] = c

ans = float('inf')
dist = warshallfloyd(n)
for route in permutations(town, r):
    bfo, tmp = route[0], 0
    for i in route[1:]:
        tmp += dist[bfo - 1][i - 1]
        bfo = i
    ans = min(ans, tmp)
print(ans)
