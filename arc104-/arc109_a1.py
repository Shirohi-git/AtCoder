a, b, x, y = map(int, input().split())

tmp = abs(a - b) - (a > b)
ans = x + tmp * min(y, 2 * x)
print(ans)
