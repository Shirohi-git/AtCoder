class LazySegtree():

    def segfunc(self, x, y):
        return max(x, y)

    def ruq_or_raq(self, k, x):
        self.lazy[k] = x
        self.data[k] = x

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
            self.ruq_or_raq(2 * i, v)
            self.ruq_or_raq(2 * i + 1, v)
            self.lazy[i] = None

    def __init__(self, LIST, ELE):
        n, self.ide_ele = len(LIST), ELE
        self.num = 1 << (n - 1).bit_length()
        self.data = [ELE] * 2 * self.num
        self.lazy = [None] * 2 * self.num
        for i in range(n):
            self.data[self.num + i] = LIST[i]
        for i in range(self.num - 1, 0, -1):
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])

    def update(self, l, r, x):
        ids = self.gindex(l, r)
        self.propagates(ids)
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                self.ruq_or_raq(l, x)
                l += 1
            if r & 1:
                self.ruq_or_raq(r - 1, x)
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

def main():
    lseg = LazySegtree([0] * W, 0)
    for l, r in LR:
        ans = lseg.query(l-1, r)+1
        lseg.update(l-1, r, ans)
        print(ans)
    return


if __name__ == '__main__':
    W, N = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(N)]

    main()
