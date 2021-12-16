def cmb(N, R):
    if (R < 0) or (N < R):
        return 0
    R = min(R, N - R)
    fact, inv = 1, 1
    for i in range(1, R + 1):
        fact = (fact * (N - i + 1)) % MOD9
        inv = (inv * i) % MOD9
    return fact * pow(inv, MOD9 - 2, MOD9) % MOD9


d = int(input())
MOD9 = 998244353

print(cmb(2 * d, d) * pow(2, MOD9 - 2, MOD9) % MOD9)
