# 2次元累積和
class Accumulate_2d:
    def __init__(self, n0, m0, lst_2d):
        self.acc_2d = [[0] * (m0+1)]
        for i in range(n0):
            acc_1d = [0]
            for lij in lst_2d[i]:
                acc_1d += [acc_1d[-1] + lij]
            self.acc_2d.append(acc_1d)
            for j in range(m0+1):
                self.acc_2d[i+1][j] += self.acc_2d[i][j]

    def query(self, sx, tx, sy, ty):
        ac2d = self.acc_2d
        res = ac2d[tx-1][ty-1] + ac2d[sx-1][sy-1]
        res -= ac2d[sx-1][ty-1] + ac2d[tx-1][sy-1]
        return res


# 座標圧縮
class Compression():
    def __init__(self, *ite):
        ite = sum(map(list, ite), [])
        self.lst = sorted(set(ite))
        self.dic = {k: i for i, k in enumerate(self.lst)}

    def zip(self, key):
        return self.dic[key]
    
    def unzip(self, idx):
        return self.lst[idx]


# Fenwicktree # 0-indexed
class Fenwicktree():
    def __init__(self, n):
        self.n = n
        self.tree = [0] * n

    # 区間和[0, i]
    def accsum(self, i):
        i, res = i + 1, 0
        while i > 0:
            res += self.tree[i - 1]
            i -= i & -i
        return res

    # lst[i] += x
    def update(self, i, x):
        i += 1
        while i <= self.n:
            self.tree[i - 1] += x
            i += i & -i

    # 区間和[i ,j)
    def query(self, i, j):
        return self.accsum(j - 1) - self.accsum(i - 1)


# Segtree
class Segtree():
    # 区間にしたい操作 ex) max,min,gcd,lcm,sum,product
    def segfunc(self, x, y):
        return max(x, y)

    # LIST: 配列の初期値, ELE: 単位元
    def __init__(self, LIST, ELE):
        self.n, self.ide_ele = len(LIST), ELE
        n = self.n
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ELE] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = LIST[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    # k番目の値をxに更新
    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    # [l, r)のsegfuncしたものを得る
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

    # k番目の値を返す
    def getval(self, k):
        return self.tree[self.num + k]

    # 2つ同時に使う # 点更新が多い、かつ、まとめて更新してもいい場合 O(N)
    def point_update(self, k, x):
        self.tree[self.num + k] = x

    def all_update(self):
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    # print用 各indexの値がいくつになっているか
    def __str__(self):
        res = [str(self.tree[self.num + i]) for i in range(self.n)]
        return ' '.join(res)


# SparseTable # 構築 O(nlogn) クエリ O(1)
class SparseTable():
    # 区間にしたい操作 ex) max, min, gcd, lcm
    def stfunc(self, x, y):
        return min(x, y)

    def __init__(self, lst0):
        n = len(lst0)
        num = n.bit_length()
        table = [lst0] + [[-1] * n for _ in range(num - 1)]
        bfo = table[0]
        for i in range(1, num):
            pow2 = (1 << (i - 1))
            for j in range(n - (1 << i) + 1):
                table[i][j] = self.stfunc(bfo[j], bfo[j + pow2])
            bfo = table[i][:]
        self.table = table

    # [l, r)のstfuncしたものを得る
    def query(self, l, r):
        i = (r - l).bit_length() - 1
        return self.stfunc(self.table[i][l], self.table[i][r - (1 << i)])


# 遅延Segtree RMQ and (RUQ or RAQ)
class LazySegtree():
    # 区間にしたい操作 ex) max,min
    def segfunc(self, x, y):
        return min(x, y)

    # RUQ or RAQ
    def ruq_or_raq(self, k, x):
        # RUQ
        self.lazy[k] = x
        self.data[k] = x
        # RAQ
        # self.lazy[k] += x
        # self.data[k] += x

    # 伝搬する対象の区間 伝搬する対象の区間, 伝搬する必要のある最大の左閉区間 lm と右閉区間 rm
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
            l >>= 1
            r >>= 1
        while l:
            idx.append(l)
            l >>= 1
        return idx

    # 遅延伝搬処理 ids: 伝搬する対象の区間
    def propagates(self, ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.ruq_or_raq(2 * i, v)
            self.ruq_or_raq(2 * i + 1, v)
            self.lazy[i] = None

    # LIST: 配列の初期値, ELE: 単位元
    def __init__(self, LIST, ELE):
        n, self.ide_ele = len(LIST), ELE
        self.num = 1 << (n - 1).bit_length()
        self.data = [ELE] * 2 * self.num
        self.lazy = [None] * 2 * self.num
        for i in range(n):
            self.data[self.num + i] = LIST[i]
        for i in range(self.num - 1, 0, -1):
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])

    # 区間[l, r)の値をxに更新
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
            l >>= 1
            r >>= 1
        for i in ids:
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])

    # [l, r)のsegfuncしたものを得る
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
