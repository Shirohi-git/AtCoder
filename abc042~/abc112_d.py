n, m = map(int, input().split())

ans = 0
for i in range(1, int(m ** 0.5) + 1):
    if m % i == 0:
        if m // i >= n:
            ans = max(ans, i)
        if i >= n:
            ans = max(ans, m // i)
print(ans)
