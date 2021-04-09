from collections import Counter


class Eratosthenes():
    def __init__(self, N):
        self.fact = [i for i in range(N + 1)]
        for i in range(2, int(N ** 0.5) + 1):
            if self.fact[i] < i:
                continue
            for j in range(i ** 2, N + 1, i):
                self.fact[j] = i
        self.prime = [i for i in range(2, N + 1) if i == self.fact[i]]

    def factor(self, NUM):
        prime = []
        while NUM > 1:
            prime.append(self.fact[NUM])
            NUM //= self.fact[NUM]
        return Counter(prime)


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


n, m = map(int, input().split())
MOD9 = 998244353

ans = 0
era = Eratosthenes(m)
cmb = Combination(n + m, MOD9)
for i in range(1, m + 1):
    num = 1
    for cnt in era.factor(i).values():
        num *= cmb.count(n + cnt - 1, cnt)
    ans += num
print(ans % MOD9)
