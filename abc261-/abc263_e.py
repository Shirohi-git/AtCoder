class Fenwicktree():
    def __init__(self, n, ini=None):
        self.n = n
        self.tree = [0] * n
        if ini:
            for i, ni in enumerate(ini):
                self.update(i, ni)

    def accsum(self, i):
        i, res = i + 1, 0
        while i > 0:
            res += self.tree[i - 1]
            i -= i & -i
        return res

    def update(self, i, x):
        i += 1
        while i <= self.n:
            self.tree[i - 1] += x
            i += i & -i

    def query(self, i, j):
        j = min(self.n, j)
        return self.accsum(j - 1) - self.accsum(i - 1)

    def __setitem__(self, key, val):
        return self.update(key, val-self.query(key, key+1))

    def __getitem__(self, key): return self.query(key, key+1)


def main():
    bit = Fenwicktree(N)
    a_inv = [pow(ai, MOD9-2, MOD9) for ai in A]
    for i, ai in [*enumerate(A)][::-1]:
        res = bit.query(i+1, i+ai+1)
        bit[i] = (res+ai+1) * a_inv[i] % MOD9
    return print(bit[0])


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    MOD9 = 998244353

    main()
