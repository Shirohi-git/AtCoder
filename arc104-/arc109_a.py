a, b, x, y = map(int, input().split())

tmp = abs(a - b)
if a == b:
    print(x)
if a > b:
    print(min(x + (tmp - 1) * y, x * (2 * tmp - 1)))
if a < b:
    print(min(x + tmp * y, x * (2 * tmp + 1)))
