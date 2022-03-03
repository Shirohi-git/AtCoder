def extgcd(a, b):
    is_mn_a, is_mn_b = 0, 0
    if a < 0:
        a, is_mn_a = abs(a), 1
    if b < 0:
        b, is_mn_b = abs(b), 1
        
    x, y, u, v = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x, u = u, x - q * u
        y, v = v, y - q * v

    x -= 2 * is_mn_a * x
    y -= 2 * is_mn_b * y
    return a, x, y


def main(x, y, p, q):
    ans = INF
    z, r = 2*(x+y), p+q
    g, m, n = extgcd(z, -r)
    for yi in range(y):
        div, mod = divmod(p - (x+yi), g)
        if mod == 0:
            ans = min(ans, div*n*r + p)
    for qi in range(q):
        div, mod = divmod(p+qi - x, g)
        if mod == 0:
            ans = min(ans, div*m*z + x)
    return print(ans if ans < INF else "infinity")

if __name__ == '__main__':
    T = int(input())
    XYPQ = [map(int, input().split()) for _ in range(T)]
    INF = float('inf')

    for i in range(T):
        main(*XYPQ[i])
