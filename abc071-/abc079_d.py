from itertools import permutations


def warshallfloyd(N, DIST):  # ワーシャルフロイド法:全頂点対最短経路 O(n**3)
    # DIST:隣接行列
    for k in range(N):
        for i in range(N):
            for j in range(N):
                DIST[i][j] = min(DIST[i][j], DIST[i][k] + DIST[k][j])
    return DIST


h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
a = [list(map(int, input().split())) for _ in range(h)]

ans, dist = 0, warshallfloyd(10, c)
for ai in a:
    for aij in ai:
        if aij != -1:
            ans += dist[aij][1]
print(ans)
