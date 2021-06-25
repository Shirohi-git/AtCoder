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


def convolve_MOD(a, b):
    mod = 998244353
    g, e = pow(3, 119, mod), 24
    ginv = pow(g, mod-2, mod)

    def FMT(lst, inv=False):
        res = lst[:]
        for i in range(n):
            j = 0
            for k in range(n_lenbit):
                j |= ((i >> k) & 1) << (n_lenbit - 1 - k)
            if (i < j):
                res[i], res[j] = res[j], res[i]

        for i in range(n_lenbit):
            w = 1
            wp = Winv[e-2-i] if inv else W[e-2-i]
            pow2i = (1 << i)

            for j in range(pow2i):
                for k in range(1 << (n_lenbit-i-1)):
                    idx = k * pow2i*2 + j
                    s, t = res[idx], res[idx + pow2i] * w
                    res[idx], res[idx + pow2i] = (s + t) % mod, (s - t) % mod
                w = (w * wp) % mod

        if (inv):
            n_inv = pow(n, mod-2, mod)
            res = [ri * n_inv % mod for ri in res]
        return res

    W, Winv = [g], [ginv]
    for _ in range(e):
        W.append(W[-1]**2 % mod)
        Winv.append(Winv[-1]**2 % mod)
    len_ab = len(a) + len(b) - 1
    n = 1 << len_ab.bit_length()
    n_lenbit = (n-1).bit_length()
    a += [0] * (n-len(a))
    b += [0] * (n-len(b))

    res = [ai * bi % mod for ai, bi in zip(FMT(a), FMT(b))]
    res = FMT(res, inv=True)[:len_ab]
    return res


def main():
    cmb = Combination(max(R, G, B), MOD9)
    cmbR = [cmb.count(R, i) if (K-Y <= i) else 0 for i in range(R+1)]
    cmbG = [cmb.count(G, i) if (K-Z <= i) else 0 for i in range(G+1)]
    cmbB = [cmb.count(B, i) if (K-X <= i) else 0 for i in range(B+1)]

    ans = 0
    cmbRG = convolve_MOD(cmbR, cmbG)
    for i in range(K+1):
        if len(cmbRG) > i and B >= K-i:
            ans += cmbRG[i] * cmbB[K-i]
            ans %= MOD9
    return print(ans)


if __name__ == '__main__':
    R, G, B, K = map(int, input().split())
    X, Y, Z = map(int, input().split())
    MOD9 = 998244353

    main()
