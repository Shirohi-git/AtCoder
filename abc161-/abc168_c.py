from math import cos, pi

a, b, h, m = map(int, input().split())

rad = abs(m * pi / 30 - (h * 60 + m) * pi / 360)
ans = a ** 2 + b ** 2 - 2 * a * b * cos(rad)
print(ans ** 0.5)
