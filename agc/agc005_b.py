class Segtree():

    def segfunc(self, x, y):
        return max(x, y) if self.wheremax else min(x, y)

    def __init__(self, LIST, ELE, WHEREMAX):
        self.wheremax = WHEREMAX
        n, self.ide_ele = len(LIST), ELE
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ELE] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = LIST[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


n = int(input())
a = list(map(int, input().split()))

idlst = [-1]*n
for i, ai in enumerate(a):
    idlst[ai-1] = i
maxseg = Segtree([-1]*n, -1, 1)
minseg = Segtree([n]*n, n, 0)

ans = 0
for i in range(n):
    idx = idlst[i]
    l = maxseg.query(0, idx)
    r = minseg.query(idx, n)
    maxseg.update(idx, idx)
    minseg.update(idx, idx)
    ans += (i+1) * (idx-l) * (r-idx)
print(ans)
