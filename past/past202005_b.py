n, m, q = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(q)]

cnt, ans = [n] * m, [[0] * m for i in range(n)]
for l in s:
    if len(l) == 2:
        print(sum([cnt[i] * ans[l[1]-1][i] for i in range(m)]))
    if len(l) == 3:
        ans[l[1] - 1][l[2] - 1] = 1
        cnt[l[2] - 1] -= 1
