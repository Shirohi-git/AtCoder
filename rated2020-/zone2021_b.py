n, d, h = map(int, input().split())
dh = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for di, hi in dh:
    a = (h-hi)/(d-di)
    b = h - a*d
    ans = max(ans, b)
print(ans)
