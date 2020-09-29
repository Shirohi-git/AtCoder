class Segtree():

    def segfunc(self, x, y):
        return x | y

    def __init__(self):
        self.ide_ele = 0
        self.num = 1 << (n - 1).bit_length()
        self.tree = [0] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = pow(2, ord(s[i]) - ord('a'))
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


n, s, q = int(input()), list(input()), int(input())
query = [input().split() for _ in range(q)]

seg = Segtree()
for num, il, cr in query:
    if num == '1':
        seg.update(int(il) - 1, pow(2, ord(cr) - ord('a')))
    elif num == '2':
        tmp = seg.query(int(il) - 1, int(cr))
        ans = sum(1 & (tmp >> i) for i in range(26))
        print(ans)
