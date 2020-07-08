def bigcmb(N, R, MOD):  # nCr(mod p) #n>=10**7,r<=10**6 #前処理不要
    if (R < 0) or (N < R):
        return 0
    R = min(R, N - R)
    fact, inv = 1, 1
    for i in range(1, R + 1):
        fact = (fact * (N - i + 1)) % MOD
        inv = (inv * i) % MOD
    return fact * pow(inv, MOD - 2, MOD) % MOD


x, y = map(int, input().split())
mod = 10 ** 9 + 7

if (x + y) % 3 != 0:
    print(0)
else:
    cnt = (x + y) // 3
    print(bigcmb(cnt, x - cnt, mod))
