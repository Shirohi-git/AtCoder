from math import ceil

r, x, y = map(int, input().split())

d2 = x ** 2 + y ** 2
print(2 if d2 < r**2 else ceil(d2 ** 0.5 / r))
