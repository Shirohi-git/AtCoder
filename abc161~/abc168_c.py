import math
a, b, h, m = map(int, input().split())

hrad, mrad = math.pi * (60 * h + m) / 360, math.pi * m / 30
rad = min(abs(hrad - mrad), 2 * math.pi - abs(hrad - mrad))

print((a ** 2 + b ** 2 - 2 * a * b * math.cos(rad)) ** 0.5)
