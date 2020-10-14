n, m = map(int, input().split())

ans = 0
for i in range(1, int(m ** 0.5) + 1):
    if m % i == 0:
        ans = max(ans, i * (m // i >= n), m // i * (i >= n))
print(ans)
