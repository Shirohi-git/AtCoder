def extgcd(a, b):  # 拡張互除法
    x, y, u, v = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x, u = u, x - q * u
        y, v = v, y - q * v
    return a, x, y

t = int(input())
xypq = [list(map(int, input().split())) for _ in range(t)]

for x, y, p, q in xypq:
    if (p + q) % 2 * (x + y) == 0:
        print('infinity')
        continue
    
