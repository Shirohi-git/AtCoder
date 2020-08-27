from itertools import product

n, m = map(int, input().split())
xyz = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for a, b, c in product([1, -1], repeat=3):
    tmp = sorted([a * x + b * y + c * z for x, y, z in xyz])
    ans = max(ans, sum(tmp[n - m:]))
print(ans)
