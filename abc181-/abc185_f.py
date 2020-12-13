class Segtree():

    def segfunc(self, x, y):
        return x ^ y

    def __init__(self, LIST, ELE):
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


n, q = map(int, input().split())
a = list(map(int, input().split()))
txy = [list(map(int, input().split())) for _ in range(q)]

seg = Segtree(a, 0)
for t, x, y in txy:
    if t == 1:
        tmp = seg.query(x - 1, x)
        seg.update(x - 1, tmp ^ y)
    if t == 2:
        print(seg.query(x - 1, y))
