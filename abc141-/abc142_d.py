def factorize(N):  # 素因数分解
    p, PRIME = 2, set()
    while p * p <= N:
        if N % p == 0:
            N //= p
            PRIME.add(p)
        else:
            p += 1
    if N > 1:
        PRIME.add(N)
    return PRIME


a, b = map(int, input().split())

ans = factorize(a) & factorize(b)
print(len(ans) + 1)
