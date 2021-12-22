class Combination():

    def __init__(self, N, MOD):
        self.mod = MOD
        self.FACT = [1, 1]
        self.INV = [0, 1]
        self.FACTINV = [1, 1]
        for i in range(2, N + 1):
            self.FACT.append((self.FACT[-1] * i) % self.mod)
            self.INV.append(pow(i, self.mod - 2, self.mod))
            self.FACTINV.append((self.FACTINV[-1] * self.INV[-1]) % self.mod)

    def count(self, N, R):
        if (R < 0) or (N < R):
            return 0
        R = min(R, N - R)
        div = self.FACTINV[R] * self.FACTINV[N-R] % self.mod
        return self.FACT[N] * div % self.mod


def main():
    powh, poww = 1, 1
    dph, dpw = [(SX == TX)], [(SY == TY)]
    for i in range(K):
        dph += [powh - dph[-1]]
        dpw += [poww - dpw[-1]]
        powh = powh * (H-1) % MOD9
        poww = poww * (W-1) % MOD9
    cmb = Combination(K, MOD9)

    ans = 0
    for i in range(K+1):
        cnt = dph[i] * dpw[K-i] % MOD9
        ans = (ans + cnt * cmb.count(K, i)) % MOD9
    return print(ans)


if "__main__":
    H, W, K = map(int, input().split())
    SX, SY, TX, TY = map(int, input().split())
    MOD9 = 998244353

    main()
