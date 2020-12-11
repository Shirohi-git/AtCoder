class LazySegtree:  # 遅延Segtree

    def segfunc(self, x, y):  # 区間にしたい操作
        return x + y  # ex) max,min,gcd,lcm,sum,product

    def __init__(self, LIST, ELE):  # LIST: 配列の初期値, ELE: 単位元
        n = len(LIST)
        self.ide_ele = ELE
        self.num = 1 << (n - 1).bit_length()
        self.data = [ELE] * 2 * self.num
        self.lazy = [None] * 2 * self.num
        for i in range(n):
            self.data[self.num + i] = LIST[i] * cnt[self.num + i]
        for i in range(self.num - 1, 0, -1):
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])

    def gindex(self, l, r):  # 伝搬する対象の区間
        """
        lm: 伝搬する必要のある最大の左閉区間
        rm: 伝搬する必要のある最大の右開区間
        """
        l += self.num
        r += self.num
        lm = l >> (l & -l).bit_length()
        rm = r >> (r & -r).bit_length()

        while r > l:
            if l <= lm:
                yield l
            if r <= rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1

    def propagates(self, *ids):  # 遅延伝搬処理 ids: 伝搬する対象の区間
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[2 * i] = v
            self.lazy[2 * i + 1] = v
            self.data[2 * i] = v * cnt[2 * i]
            self.data[2 * i + 1] = v * cnt[2 * i + 1]
            self.lazy[i] = None

    def update(self, l, r, x):  # 区間[l, r)の値をxに更新
        *ids, = self.gindex(l, r)
        self.propagates(*ids)
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                self.lazy[l] = x
                self.data[l] = x * cnt[l]
                l += 1
            if r & 1:
                self.lazy[r - 1] = x
                self.data[r - 1] = x * cnt[r - 1]
            r >>= 1
            l >>= 1
        for i in ids:
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])

    def query(self, l, r):  # [l, r)のsegfuncしたものを得る
        *ids, = self.gindex(l, r)
        self.propagates(*ids)
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(self.data[l], res)
                l += 1
            if r & 1:
                res = self.segfunc(res, self.data[r - 1])
            l >>= 1
            r >>= 1
        return res


n, q = map(int, input().split())
lrd = [list(map(int, input().split())) for _ in range(q)]
MOD = 998244353

cnt = tmp = [pow(10, i, MOD) for i in range(pow(2, (n - 1).bit_length()))]
num = 1
for j in range((n - 1).bit_length()):
    num = int(str(num) * 2)
    tmp = [tmp[i] for i in range(0, len(tmp), 2)]
    cnt += [num * ti % MOD for ti in tmp]
cnt = [0] + cnt[::-1]

lseg = LazySegtree([1] * n, 0)
for l, r, d in lrd:
    lseg.update(l - 1, r, d)
    print(int(lseg.query(0, n)) % MOD)
