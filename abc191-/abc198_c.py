from math import ceil

r, x, y = map(int, input().split())

d2 = x ** 2 + y ** 2
if d2 != r ** 2 and d2 <= 4 * r ** 2:
    print(2)
else:
    print(ceil(d2 ** 0.5 / r))
