class LazySegtree:

    def segfunc(self, x, y):
        return (x + y) % MOD

    def __init__(self, ELE):
        self.ide_ele = ELE
        self.num = 1 << (n - 1).bit_length()
        self.size = [0] * 2 * self.num
        for i in range(n):
            self.size[self.num + i] = pow(10, n - 1 - i, MOD)
        for i in range(self.num - 1, 0, -1):
            self.size[i] = self.segfunc(self.size[2 * i], self.size[2 * i + 1])
        self.data = self.size[:]
        self.lazy = [None] * 2 * self.num

    def gindex(self, l, r):
        l += self.num
        r += self.num
        lm = l >> (l & -l).bit_length()
        rm = r >> (r & -r).bit_length()

        idx = []
        while r > l:
            if l <= lm:
                idx.append(l)
            if r <= rm:
                idx.append(r)
            r >>= 1
            l >>= 1
        while l:
            idx.append(l)
            l >>= 1
        return idx

    def propagates(self, ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[2 * i] = v
            self.lazy[2 * i + 1] = v
            self.data[2 * i] = v * self.size[2 * i]
            self.data[2 * i + 1] = v * self.size[2 * i + 1]
            self.lazy[i] = None

    def update(self, l, r, x):
        ids = self.gindex(l, r)
        self.propagates(ids)
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                self.lazy[l] = x
                self.data[l] = x * self.size[l]
                l += 1
            if r & 1:
                self.lazy[r - 1] = x
                self.data[r - 1] = x * self.size[r - 1]
            r >>= 1
            l >>= 1
        for i in ids:
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])

    def query(self, l, r):
        ids = self.gindex(l, r)
        self.propagates(ids)
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.data[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.data[r - 1])
            l >>= 1
            r >>= 1
        return res


n, q = map(int, input().split())
lrd = [list(map(int, input().split())) for _ in range(q)]
MOD = 998244353

lseg = LazySegtree(0)
for l, r, d in lrd:
    lseg.update(l - 1, r, d)
    print(int(lseg.query(0, n)) % MOD)
