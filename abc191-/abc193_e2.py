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


def crt(num_mod):
    res, mod = num_mod[0]
    for ni, mi in num_mod:
        g, m, n = extgcd(mod, mi)
        if (res - ni) % g:
            return 0, -1
        mod = mod * mi // g
        div = (res - ni) // g
        res = (div * n * mi + ni) % mod
    return res, mod


def main(x, y, p, q):
    ans = INF
    z, r = 2*(x+y), p+q
    for xyi in range(x, x+y):
        a, m = crt([[xyi, z], [p, r]])
        if m > 0:
            ans = min(a, ans)
    for pqi in range(p, p+q):
        a, m = crt([[x, z], [pqi, r]])
        if m > 0:
            ans = min(a, ans)
    return print(ans if ans < INF else "infinity")


if __name__ == '__main__':
    T = int(input())
    XYPQ = [map(int, input().split()) for _ in range(T)]
    INF = 10**20

    for i in range(T):
        main(*XYPQ[i])
