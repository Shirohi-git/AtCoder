class Combination():
    def __init__(self, N):
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


n, k = map(int, input().split())
MOD = 10 ** 9 + 7

cmb = Combination(n)
ans = 0
for i in range(min(k + 1, n)):
    ans += cmb.count(n, i) * cmb.count(n - 1, i)
    ans %= MOD
print(ans)
