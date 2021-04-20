class Segtree():  # Segtree

    def segfunc(self, x, y):  # 区間にしたい操作
        return min(x, y)  # ex) max,min,gcd,lcm,sum,product

    def __init__(self, LIST, ELE):  # LIST: 配列の初期値, ELE: 単位元
        self.ide_ele = ELE
        self.num = 1 << (len(LIST) - 1).bit_length()
        self.tree = [ELE] * 2 * self.num
        for i in range(len(LIST)):
            self.tree[self.num + i] = LIST[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):  # k番目の値をxに更新
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):  # [l, r)のsegfuncしたものを得る
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


n, m = map(int, input().split())
lrc = sorted(tuple(map(int, input().split())) for _ in range(m))

lst = [0] + [10 ** 15] * (n - 1)
pow2 = 1 << (n - 1).bit_length()
seg = Segtree(lst, 10 ** 15)
for l, r, c in lrc:
    tmp = seg.query(l - 1, r) + c
    seg.update(r - 1, min(seg.tree[pow2 + r - 1], tmp))
ans = seg.query(n - 1, n)
print(-1 if ans == 10 ** 15 else ans)
