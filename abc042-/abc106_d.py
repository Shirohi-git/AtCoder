n, m, q = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(m)]
pq = [list(map(int, input().split())) for _ in range(q)]

acc = [[0] * (n + 1) for _ in range(n + 1)]
for l, r in lr:
    acc[l][r] += 1
for i in range(n):
    for j in range(n):
        tmp = acc[i][j + 1] + acc[i + 1][j] - acc[i][j]
        acc[i + 1][j + 1] += tmp

for p, q in pq:
    p -= 1
    ans = acc[q][q] - acc[p][q] - acc[q][p] + acc[p][p]
    print(ans)
