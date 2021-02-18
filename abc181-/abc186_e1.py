from math import gcd


def totient(N):
    p, phi = 2, N
    while p * p <= N:
        if N % p == 0:
            phi = phi // p * (p - 1)
        while N % p == 0:
            N //= p
        p += 1
    if N > 1:
        phi = phi // N * (N - 1)
    return phi


t = int(input())
nsk = [list(map(int, input().split())) for _ in range(t)]

# 解説AC ver.1 オイラーの定理
for n, s, k in nsk:
    tmp = gcd(gcd(n, s), k)
    n, s, k = map(lambda x: x // tmp, [n, s, k])
    ans = -s * pow(k, totient(n) - 1, n) % n
    print(ans if gcd(n, k) == 1 else - 1)
