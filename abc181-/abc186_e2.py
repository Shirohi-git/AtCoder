from math import gcd


def extgcd(a, b):
    x, y, u, v = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x, u = u, x - q * u
        y, v = v, y - q * v
    return a, x

t = int(input())
nsk = [list(map(int, input().split())) for _ in range(t)]

# 解説AC ver.2 拡張互除法
for n, s, k in nsk:
    tmp = gcd(gcd(n, s), k)
    n, s, k = map(lambda x: x // tmp, [n, s, k])
    res, x = extgcd(k, n)
    print(-s * x % n if res == 1 else - 1)
