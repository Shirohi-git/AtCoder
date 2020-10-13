n, a, b, c, d = map(int, input().split())

DIFF, ans = b - a, False
for i in range(n):
    j = n - 1 - i
    if c * j - d * i <= DIFF <= d * j - c * i:
        ans = True
print('YES' if ans else 'NO')
