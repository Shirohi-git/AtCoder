n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans, stp, nxt = n, [0] * m, [0] * n
for _ in range(m):
    cnt = [0] * m
    for i, ai in enumerate(a):
        while stp[ai[nxt[i]] - 1]:
            nxt[i] += 1
        cnt[ai[nxt[i]] - 1] += 1
    res, spo = max((cnt[j], j) for j in range(m))
    ans, stp[spo] = min(ans, res), 1
print(ans)
