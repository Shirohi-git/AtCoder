n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for ai in a:
    cnt = sum(aij * bi for aij, bi in zip(ai, b))
    ans += (cnt > -c)
print(ans)
