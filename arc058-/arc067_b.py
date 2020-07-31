n, a, b = map(int, input().split())
x = list(map(int, input().split()))

ans, now = 0, x[0]
for i in x[1:]:
    ans += min(a * (i - now), b)
    now = i
print(ans)
