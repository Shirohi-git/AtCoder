from itertools import combinations

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for (px, py), (qx, qy), (rx, ry) in combinations(xy, 3):
    a1, a2 = (py - qy) * (px - rx), (py - ry) * (px - qx)
    ans |= (a1 == a2)
print('Yes' if ans else 'No')
