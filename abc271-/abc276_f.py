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
        if i >= self.n:
            raise IndexError
        j = min(self.n, j)
        return self.accsum(j - 1) - self.accsum(i - 1)

    def __setitem__(self, key, val):
        return self.update(key, val - self.query(key, key+1))

    def __getitem__(self, key): return self.query(key, key+1)


def main():
    cnt, val = Fenwicktree(MAX), Fenwicktree(MAX)
    ans = []
    res = 0
    for i, ai in enumerate(A, 1):
        res += 2 * ai * cnt.query(0, ai)
        res += 2 * val.query(ai, MAX) + ai
        res %= MOD9
        cnt[ai] += 1
        val[ai] += ai
        ans.append(res * pow(i**2, MOD9-2, MOD9) % MOD9)
    return print(*ans, sep='\n')


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    MOD9 = 998244353
    MAX = max(A) + 1

    main()
