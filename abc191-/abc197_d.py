from math import sin, cos, pi

n = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())

cx, cy = (ax + bx) / 2, (ay + by) / 2
rad = 2 * pi / n
qx = (ax - cx) * cos(rad) - (ay - cy) * sin(rad) + cx
qy = (ax - cx) * sin(rad) + (ay - cy) * cos(rad) + cy
print(qx, qy)
