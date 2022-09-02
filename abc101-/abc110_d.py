from collections import Counter


class Enumeration:
    def __init__(self, N, MOD):
        self.mod = MOD
        self.FACT = [1, 1]
        self.INV = [0, 1]
        self.FACTINV = [1, 1]
        for i in range(2, N + 1):
            self.FACT.append((self.FACT[-1] * i) % self.mod)
            self.INV.append(pow(i, self.mod - 2, self.mod))
            self.FACTINV.append((self.FACTINV[-1] * self.INV[-1]) % self.mod)

    def combination(self, N, R):
        if (R < 0) or (N < R):
            return 0
        R = min(R, N - R)
        div = self.FACTINV[R] * self.FACTINV[N-R] % self.mod
        return self.FACT[N] * div % self.mod


def main():
    def factorize(n0):
        p, res = 2, []
        while p * p <= n0:
            while n0 % p == 0:
                n0 //= p
                res.append(p)
            p += 1
        if n0 > 1:
            res.append(n0)
        return res

    prime = Counter(factorize(M))
    cmb = Enumeration(N+31, MOD1)

    ans = 1
    for c in prime.values():
        ans *= cmb.combination(c + (N-1), c)
        ans %= MOD1
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    MOD1 = 10**9 + 7

    main()
