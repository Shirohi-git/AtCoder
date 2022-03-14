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


class Convolve_MOD:
    def __init__(self):
        self.mod = mod = 998244353
        self.g, self.e = g, e = pow(3, 119, mod), 24
        self.ginv = ginv = pow(g, mod-2, mod)

        self.W, self.Winv = [g], [ginv]
        for _ in range(e):
            self.W.append(self.W[-1]**2 % mod)
            self.Winv.append(self.Winv[-1]**2 % mod)

    def FMT(self, lst, inv=False):
        res = lst[:]
        for i in range(self.n):
            j = 0
            for k in range(self.n_lenbit):
                j |= ((i >> k) & 1) << (self.n_lenbit - 1 - k)
            if (i < j):
                res[i], res[j] = res[j], res[i]

        for i in range(self.n_lenbit):
            w, wp = 1, self.W[self.e - 2 - i]
            if inv:
                wp = self.Winv[self.e - 2 - i]
            pow2i = (1 << i)

            for j in range(pow2i):
                for k in range(1 << (self.n_lenbit - i-1)):
                    idx = k * pow2i*2 + j
                    s, t = res[idx], res[idx + pow2i] * w
                    res[idx] = (s + t) % self.mod
                    res[idx + pow2i] = (s - t) % self.mod
                w = (w * wp) % self.mod

        if (inv):
            n_inv = pow(self.n, self.mod-2, self.mod)
            res = [ri * n_inv % self.mod for ri in res]
        return res

    def convolve(self, x, y):
        a, b = x[:], y[:]
        len_ab = len(a) + len(b) - 1
        self.n = n = 1 << len_ab.bit_length()
        self.n_lenbit = (n-1).bit_length()
        a += [0] * (n-len(a))
        b += [0] * (n-len(b))

        res = [ai * bi % self.mod for ai, bi in zip(self.FMT(a), self.FMT(b))]
        res = self.FMT(res, inv=True)[:len_ab]
        return res


def main():
    if M > K:
        return print(0)

    def conv_lst(ele):
        ele = ele * w_suminv % MOD9
        res = [[1], [0]]
        for i in range(1, K+1):
            res[1] += [pow(ele, i, MOD9) * cmb.FACTINV[i] % MOD9]
        return res

    w_suminv = pow(sum(W), MOD9-2, MOD9)
    cmb = Combination(K, MOD9)
    cnv_mod = Convolve_MOD()
    cnv = [[1]]
    for wi in W:
        now = conv_lst(wi)
        nxt = [[0] * (K+1) for _ in range(M+1)]
        for i in range(len(now)):
            for j in range(len(cnv)):
                if i+j > M:
                    break
                tmp = cnv_mod.convolve(cnv[j], now[i])
                nxt[i+j] = [nk + tk for nk, tk in zip(nxt[i+j], tmp)]
        cnv = [ni[:] for ni in nxt]
    ans = cnv[M][K] * cmb.FACT[K] % MOD9
    return print(ans)


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    W = [int(input()) for _ in range(N)]
    MOD9 = 998244353

    main()
