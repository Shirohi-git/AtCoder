def pre_cmb(N, MOD):
    FACT = [1, 1]  # 階乗
    INV = [0, 1]  # 各iの逆元
    FACTINV = [1, 1]  # 階乗の逆元

    for i in range(2, N + 1):
        FACT.append((FACT[-1] * i) % MOD)
        INV.append(pow(i,MOD-2,MOD))
        FACTINV.append((FACTINV[-1] * INV[-1]) % MOD)
    PRELIST = FACT, FACTINV
    return PRELIST


def cmb(N, R, MOD, PRELIST):
    FACT, FACTINV = PRELIST
    if (R < 0) or (N < R):
        return 0
    R = min(R, N - R)
    return FACT[N] * FACTINV[R] * FACTINV[N-R] % MOD


n, m, k = map(int, input().split())
mod = 998244353

prelist = pre_cmb(n, mod)

cnt = 0
for i in range(k + 1):
    cnt += (m * pow(m - 1, n - i - 1, mod) * cmb(n - 1, i, mod, prelist)) % mod

print(cnt % mod)
