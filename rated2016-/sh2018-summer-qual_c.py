n, m, d = map(int, input().split())

tmp = (m - 1) * (n - d) / n ** 2
print(tmp * (1 + (d > 0)))
