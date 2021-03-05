v, t, s, d = map(int, input().split())
res = 1 - (v * t <= d <= v * s)
print('Yes' if res else 'No')
