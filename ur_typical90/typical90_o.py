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
        return self.FACT[N] * self.FACTINV[R] * self.FACTINV[N-R] % self.mod


n = int(input())
MOD1 = 10**9 + 7

cmb = Combination(n, MOD1)
for i in range(1, n+1):
    ans, sup = 0, (n-1) // i + 1
    for j in range(sup):
        ans += cmb.count(n - i*j + j, j+1)
    print(ans % MOD1)
