from itertools import product

n, m, x = map(int, input().split())
ca = [list(map(int, input().split())) for _ in range(n)]

ans = float('inf')
for l in product([0, 1], repeat=n):
    a = [0] * m
    cnt = 0
    for i, buy in enumerate(l):
        if buy == 1:
            cnt += ca[i][0]
            for j in range(1, m + 1):
                a[j - 1] += ca[i][j]
    if all(i >= x for i in a):
        ans = min(ans, cnt)

print(-1 if ans == float('inf') else ans)
