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
    from collections import Counter
    
    cnt = Counter(S)
    fact = [1]
    for i in range(N):
        fact.append(fact[-1] * (i+1))
    finv = [pow(fi, MOD9-2, MOD9) for fi in fact]
    
    cmb = finv[:cnt[Alp[0]]+1]
    for j in Alp[1:]:
        cmb = convolve_MOD(cmb, finv[:cnt[j]+1])
    ans = sum(fact[i] * cmb[i] for i in range(1, N+1))
    return print(ans % MOD9)


if __name__ == '__main__':
    S = input()
    N = len(S)
    MOD9 = 998244353
    Alp = "abcdefghijklmnopqrstuvwxyz"

    main()