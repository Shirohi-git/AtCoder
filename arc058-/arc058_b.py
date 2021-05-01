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


h, w, a, b = map(int, input().split())
MOD1 = 10**9 + 7

ans = 0
cmb = Combination(h+w, MOD1)
for i in range(h-a):
    h2, w2 = h-1-i, w-b-1
    ans += cmb.count(i + b-1, i) * cmb.count(w2 + h2, h2)
    ans %= MOD1
print(ans)
