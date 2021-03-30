n, s, d = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]

res = 0
for x, y in xy:
    res |= (x < s) & (y > d)
print('Yes' if res else 'No')
