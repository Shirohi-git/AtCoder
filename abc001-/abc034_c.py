def bigcmb(N, R, MOD):
    if (R < 0) or (N < R):
        return 0
    R = min(R, N - R)
    fact, inv = 1, 1
    for i in range(1, R + 1):
        fact = (fact * (N - i + 1)) % MOD
        inv = (inv * i) % MOD
    return fact * pow(inv, MOD - 2, MOD) % MOD

w, h = map(int, input().split())
print(bigcmb(h + w - 2, h - 1, 10 ** 9 + 7))
