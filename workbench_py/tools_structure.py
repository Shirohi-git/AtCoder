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
class Compression:
    def __init__(self, *ite):
        ite = sum(map(list, ite), [])
        self.lst = sorted(set(ite))
        self.dic = {k: i for i, k in enumerate(self.lst)}
        self.len = len(self.lst)

    def zip(self, key):
        return self.dic[key]

    def unzip(self, idx):
        return self.lst[idx]


# 非再帰AVL-tree
# https://stnkien.hatenablog.com/entry/avl-tree
class AVL_Tree:
    class Node:
        """ノード

        Attributes:
            key (any): ノードのキー。比較可能なものであれば良い。(1, 4)などタプルも可。
            val (any): ノードの値。
            l_node (Node): 左の子ノード。
            r_node (Node): 右の子ノード。
            bias (int): 平衡度。(左部分木の高さ)-(右部分木の高さ)。
            size (int): 自分を根とする部分木の大きさ

        """

        def __init__(self, key, val):
            self.key, self.val = key, val
            self.l_node = self.r_node = None
            self.bias, self.size = 0, 1

    def __init__(self):
        self.root = None

    def __rotate_left(self, v):
        u = v.r_node
        u.size = v.size
        v.size -= 1 + (u.r_node.size if u.r_node is not None else 0)
        v.r_node, u.l_node = u.l_node, v
        if u.bias == -1:
            u.bias = v.bias = 0
        else:
            u.bias, v.bias = 1, -1
        return u

    def __rotate_right(self, v):
        u = v.l_node
        u.size = v.size
        v.size -= 1 + (u.l_node.size if u.l_node is not None else 0)
        v.l_node, u.r_node = u.r_node, v
        if u.bias == 1:
            u.bias = v.bias = 0
        else:
            u.bias, v.bias = -1, 1
        return u

    def __update_bias_double(self, v):
        if v.bias == 1:
            v.r_node.bias = -1
            v.l_node.bias = 0
        elif v.bias == -1:
            v.r_node.bias = 0
            v.l_node.bias = 1
        else:
            v.r_node.bias = 0
            v.l_node.bias = 0
        v.bias = 0
        return None

    def __rotate_LR(self, v):
        u, t = v.l_node, v.l_node.r_node
        t.size = v.size
        v.size -= u.size - (t.r_node.size if t.r_node is not None else 0)
        u.size -= 1 + (t.r_node.size if t.r_node is not None else 0)
        u.r_node, t.l_node = t.l_node, u
        v.l_node, t.r_node = t.r_node, v
        self.__update_bias_double(t)
        return t

    def __rotate_RL(self, v):
        u, t = v.r_node, v.r_node.l_node
        t.size = v.size
        v.size -= u.size - (t.l_node.size if t.l_node is not None else 0)
        u.size -= t.l_node.size + 1 if t.l_node is not None else 1
        u.l_node, t.r_node = t.r_node, u
        v.r_node, t.l_node = t.l_node, v
        self.__update_bias_double(t)
        return t

    def __rotate(self, v):
        if v.bias == 2:
            if v.l_node.bias == -1:
                new_v = self.__rotate_LR(v)
            else:
                new_v = self.__rotate_right(v)

        elif v.bias == -2:
            if v.r_node.bias == 1:
                new_v = self.__rotate_RL(v)
            else:
                new_v = self.__rotate_left(v)
        return new_v

    def __set_child(self, v, vdir, c):
        if vdir == 1:
            v.l_node = c
        else:  # vdir == -1:
            v.r_node = c
        return

    def __get_node(self, key):
        v = self.root
        self.history = []
        while v is not None:
            if key == v.key:
                return v
            elif key < v.key:
                self.history.append((v, 1))
                v = v.l_node
            elif v.key < key:
                self.history.append((v, -1))
                v = v.r_node
        return None

    def insert(self, key, val=0):
        """挿入

        指定したkeyに値valを挿入する。
        その後、平衡を保つように回転を行う。

        Args:
            key (any): キー。
            val (any): 値。

        Note:
            同じキーがあった場合に上書きする。

        """
        new = self.Node(key, val)
        if self.root is None:
            self.root = new
            return

        v = self.__get_node(key)
        if v is not None:
            v.val = val
            return

        history = self.history
        self.__set_child(*history[-1], new)

        while history:
            v, v_dir = history.pop()
            v.bias += v_dir
            v.size += 1

            new_v = None
            if v.bias in [2, -2]:
                new_v = self.__rotate(v)
            elif v.bias == 0:
                break

            if new_v is not None:
                if len(history) == 0:
                    self.root = new_v
                    return
                self.__set_child(*history[-1], new_v)
                break

        while history:
            p, _ = history.pop()
            p.size += 1
        return

    def delete(self, key):
        """削除

        指定したkeyの要素を削除する。
        その後、平衡を保つように回転を行う。

        Args:
            key (any): キー。

        Return:
            bool: 指定したキーが存在するならTrue、しないならFalse。

        """
        v = self.__get_node(key)
        if v is None:
            return False

        history = self.history
        if v.l_node is not None:
            history.append((v, 1))
            lmax = v.l_node
            while lmax.r_node is not None:
                history.append((lmax, -1))
                lmax = lmax.r_node
            v.key, v.val = lmax.key, lmax.val
            v = lmax

        c = v.l_node if v.l_node is not None else v.r_node
        if history:
            self.__set_child(*history[-1], c)
        else:
            self.root = c
            return True

        while history:
            v, v_dir = history.pop()
            v.bias -= v_dir
            v.size -= 1

            new_v = None
            if v.bias in [2, -2]:
                new_v = self.__rotate(v)
            elif v.bias != 0:
                break

            if new_v is not None:
                if len(history) == 0:
                    self.root = new_v
                    return True
                self.__set_child(*history[-1], new_v)
                if new_v.bias != 0:
                    break

        while history:
            p, _ = history.pop()
            p.size -= 1
        return True

    def get(self, key):
        """値の取り出し

            指定したkeyの値を返す。
            keyが存在しない場合はNoneを返す。

            Args:
                key (any): キー。

            Return:
                any: 指定したキーが存在するならその値、存在しないならNone。

        """
        v = self.root
        while v is not None:
            if key == v.key:
                return v.val
            elif key < v.key:
                v = v.l_node
            elif v.key < key:
                v = v.r_node
        return None

    def lower_bound(self, key):
        """下限つき探索

        指定したkey以上で最小のキーを見つける。

        Args:
            key (any): キーの下限。

        Return:
            any: 条件を満たすようなキー。そのようなキーが一つも存在しないならNone。

        """
        #res = float('inf')
        res = None
        v = self.root
        while v is not None:
            if v.key >= key:
                if res is None or res > v.key:
                    res = v.key
                v = v.l_node
            else:
                v = v.r_node
        return res

    def upper_bound(self, key):
        """上限つき探索

        指定したkey未満で最大のキーを見つける。

        Args:
            key (any): キーの上限。

        Return:
            any: 条件を満たすようなキー。そのようなキーが一つも存在しないならNone。

        """
        #res = -float('inf')
        res = None
        v = self.root
        while v is not None:
            if v.key < key:
                if res is None or res < v.key:
                    res = v.key
                v = v.r_node
            else:
                v = v.l_node
        return res

    def find_Kth_element(self, k):
        """小さい方からk番目の要素を見つける

        Args:
            k (int): 何番目の要素か(0オリジン)。
        """
        v = self.root
        s = 0
        while v is not None:
            t = s + (v.l_node.size if v.l_node is not None else 0)
            if t == k:
                return v.key
            elif t < k:
                s = t + 1
                v = v.r_node
            else:
                v = v.l_node
        return None

    def __getitem__(self, key): return self.get(key)
    def __setitem__(self, key, val): return self.insert(key, val)
    def __bool__(self): return self.root is not None
    def __len__(self): return self.root.size if self.root is not None else 0


# Fenwicktree # 0-indexed
class Fenwicktree:
    def __init__(self, n, ini=None):
        self.n = n
        self.tree = [0] * n
        if ini:
            for i, ni in enumerate(ini):
                self.update(i, ni)

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
        if i >= self.n:
            raise IndexError
        j = min(self.n, j)
        return self.accsum(j - 1) - self.accsum(i - 1)

    def __setitem__(self, key, val):
        return self.update(key, val - self.query(key, key+1))

    def __getitem__(self, key): return self.query(key, key+1)

    def __str__(self):
        res = [str(self.query(k, k+1)) for k in range(self.n)]
        return "FenwickTree " + '[' + ', '.join(res) + ']'


# Segtree
class Segtree:
    # 区間にしたい操作 ex) max,min,gcd,lcm,sum,product
    def segfunc(self, x, y):
        return max(x, y)

    # LIST: 配列の初期値, ELE: 単位元
    def __init__(self, LIST, ELE):
        self.n, self.ide_ele = len(LIST), ELE
        n = self.n
        self.num = 1 << (n - 1).bit_length()
        tree = self.tree = [ELE] * 2 * self.num
        for i in range(n):
            tree[self.num + i] = LIST[i]
        for i in range(self.num - 1, 0, -1):
            tree[i] = self.segfunc(tree[2 * i], tree[2 * i + 1])

    # k番目の値をxに更新
    def update(self, k, x):
        tree = self.tree
        k += self.num
        tree[k] = x
        while k > 1:
            tree[k >> 1] = self.segfunc(tree[k], tree[k ^ 1])
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
        tree = self.tree
        for i in range(self.num - 1, 0, -1):
            tree[i] = self.segfunc(tree[2 * i], tree[2 * i + 1])

    # print用 各indexの値がいくつになっているか
    def __str__(self):
        res = [str(self.tree[self.num + i]) for i in range(self.n)]
        return ' '.join(res)


# SparseTable # 構築 O(nlogn) クエリ O(1)
class SparseTable:
    # 区間にしたい操作 ex) max, min, gcd, lcm
    def stfunc(self, x, y):
        return min(x, y)

    def __init__(self, lst0, ini):
        n = len(lst0)
        num = n.bit_length()
        table = [lst0] + [[ini] * n for _ in range(num - 1)]
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
class LazySegtree:
    # 区間にしたい操作 ex) max,min
    def segfunc(self, x, y):
        return min(x, y)

    # RUQ or RAQ
    def ruq_or_raq(self, k, x):
        # RUQ
        # """
        self.lazy[k] = x
        self.data[k] = x
        # """
        # RAQ
        """
        if self.lazy[k] is None:
            self.lazy[k] = 0
        self.lazy[k] += x
        self.data[k] += x
        """

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
