# pypyは文字列結合NG,再帰NG

# floatを使うときは大きい数に注意
# if in dict.values() はO(n)

# 入力が多い時
import sys
input = sys.stdin.readline

# 再帰の深さに注意
import sys
sys.setrecursionlimit(10 ** 7)

# 冪乗 n ** m % mod == pow(n, m, mod)
# フェルマーの小定理(pは素数, aはpと互いに素)
# pow(a, p-1, p) == 1 (mod_p) <=> pow(a, p-2, p) == a**(-1) (mod_p)
# 割り算するところを掛け算できるので先にmodが取れる


def ceil(X, Y):  # 天井関数 ceil(X/Y) Y>1
    return (X + Y - 1) // Y


def lcm(X, Y):  # 最小公倍数
    from math import gcd
    return (X * Y) // gcd(X, Y)


def bitcount(N):  # 立ってるbitの数
    bitcnt = [0]
    for _ in range(N):
        bitcnt += [i + 1 for i in bitcnt]
    return bitcnt


def extgcd(a, b):  # 拡張互除法
    x, y, u, v = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x, u = u, x - q * u
        y, v = v, y - q * v
    return a, x, y


def factorize(N):  # 素因数分解
    p, PRIME = 2, []
    while p * p <= N:
        while N % p == 0:
            N //= p
            PRIME.append(p)
        p += 1
    if N > 1:
        PRIME.append(N)
    return PRIME


def makedivisor(N):  # 約数列挙
    p, upper, lower = 1, [], []
    while p * p <= N:
        if N % p == 0:
            lower.append(p)
            if p * p != N:
                upper.append(N // p)
        p += 1
    return lower + upper[::-1]


def totient(N):  # オイラーのトーシェント関数
    p, phi = 2, N
    while p * p <= N:
        if N % p == 0:
            phi = phi // p * (p - 1)
        while N % p == 0:
            N //= p
        p += 1
    if N > 1:
        phi = phi // N * (N - 1)
    return phi


# エラトステネスの篩
class Eratosthenes():
    # 素数リスト生成 O(n*log(log n))
    def __init__(self, N):
        self.fact = [i for i in range(N + 1)]
        for i in range(2, int(N ** 0.5) + 1):
            if self.fact[i] < i:
                continue
            for j in range(i ** 2, N + 1, i):
                self.fact[j] = i
        self.prime = [i for i in range(2, N + 1) if i == self.fact[i]]

    # 高速素因数分解 O(log num)
    def factor(self, NUM):
        PRIME = set()
        while NUM > 1:
            PRIME.add(self.fact[NUM])
            NUM //= self.fact[NUM]
        return PRIME


# nCr(mod p) #n<=10**6
class Combination():
    # cmbの前処理(階乗, 各iの逆元, 階乗の逆元)
    def __init__(self, N, MOD):
        self.mod = MOD
        self.FACT = [1, 1]
        self.INV = [0, 1]
        self.FACTINV = [1, 1]
        for i in range(2, N + 1):
            self.FACT.append((self.FACT[-1] * i) % self.mod)
            self.INV.append(pow(i, self.mod - 2, self.mod))
            self.FACTINV.append((self.FACTINV[-1] * self.INV[-1]) % self.mod)

    # nCr(mod p) #前処理必要
    def count(self, N, R):
        if (R < 0) or (N < R):
            return 0
        R = min(R, N - R)
        div = self.FACTINV[R] * self.FACTINV[N-R] % self.mod
        return self.FACT[N] * div % self.mod


def bigcmb(N, R, MOD):  # nCr(mod p) #n>=10**7,r<=10**6 #前処理不要
    if (R < 0) or (N < R):
        return 0
    R = min(R, N - R)
    fact, inv = 1, 1
    for i in range(1, R + 1):
        fact = (fact * (N - i + 1)) % MOD
        inv = (inv * i) % MOD
    return fact * pow(inv, MOD - 2, MOD) % MOD


def binary(l, r):  # 二分探索 # N:探索要素数 # lは不適, rは適合
    while abs(r - l) > 1:
        mid = (l + r) // 2
        if True:  # 条件式
            r = mid
        else:
            l = mid
    return r


def knapsack(N, W, ITEM):  # ナップザック問題 # 典型dp
    # 個数,上限重さ,itemリスト
    dp = [[0] * (W + 1)] + [[-float("inf")] * (W + 1) for _ in range(N)]
    # dp = [[-float("inf")]*(W+1)] + [[-float("inf")]*(W+1) for _ in range(n)]
    # dp[0][0] = 0
    # 重さwぴったり、を求めるとき
    wei, val = 0, 1

    for i in range(N):
        for j in range(W + 1):
            tmp = dp[i][j]
            if ITEM[i][wei] <= j:
                tmp = dp[i][j - ITEM[i][wei]] + ITEM[i][val]
            dp[i + 1][j] = max(dp[i][j], tmp)
    return dp[N][W]


def memodp(DP, NEAR, x):
    if True:  # 条件式
        return DP[x]

    for i in NEAR[x]:
        DP[x] += memodp(DP, NEAR, i)
        # 漸化式
    return DP[x]


# 巡回セールスマン問題
class TSP():
    def __init__(self, n):
        self.n = n
        self.memo = [[-1] * (1 << n) for _ in range(n)]
        self.dist = [[0] * n for _ in range(n)]
        # 頂点間の距離の入力

    # s: 現在地, bit: 訪問済み
    def tspdp(self, s, bit):
        if bit == (1 << self.n) - 1:
            self.memo[s][bit] = self.dist[s][0]
            return self.dist[s][0]

        res = float('inf')
        for t in range(self.n):
            if (bit >> t) & 1:
                continue
            nxt = bit + (1 << t)
            if self.memo[t][bit] == -1:
                self.memo[t][bit] = self.tspdp(t, nxt)
            tmp = self.dist[s][t] + self.memo[t][bit]
            res = min(res, tmp)
        return res


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
        n, self.ide_ele = len(LIST), ELE
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


# SparseTable # 構築 O(nlogn) クエリ O(1)
class SparseTable():

    # 区間にしたい操作 ex) max, min, gcd,lcm
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


# 行列積
def mat_product(a, b):
    n, m, l = len(a), len(b), len(b[0])
    res = [[0] * l for _ in range(n)]
    for i in range(n):
        for j in range(l):
            for k in range(m):
                res[i][j] += a[i][k] * b[k][j]
    return res


# 行列累乗 res[i] = mat**(2**i)
def mat_powlst(cnt, mat):
    n = len(mat)
    res = [[[0] * n for _ in range(n)] for _ in range(cnt+1)]
    res[0] = [[matij for matij in mati] for mati in mat]
    for i in range(cnt):
        res[i+1] = mat_product(res[i], res[i])
    return res


def rad_to_deg(rad):
    from math import pi as PI
    return (((rad) / 2 / PI) * 360)


# 凸包
def convex_hull(point_lst):
    
    # 時計回りか # 一直線上で高々2点の場合 ">="
    def is_CW(ax, ay, bx, by, cx=0, cy=0):
        res = (bx-cx) * (ay-cy) - (by-cy) * (ax-cx)
        return res > 0

    # 半分凸包
    def half_hull(lst):
        res = []
        for pi in lst:
            while len(res) > 1 and is_CW(*pi, *res[-2], *res[-1]):
                res.pop()
            res.append(pi)
        return res

    point_lst = sorted(point_lst)
    res1 = half_hull(point_lst)
    res2 = half_hull(point_lst[::-1])
    return res1 + res2[1:]


# 畳み込み
def convolve(a, b):
    
    from math import pi as PI, cos, sin

    # 高速フーリエ変換 O(nlogn)
    def FFT(lst, inv=False):
        n = len(lst)
        num = (n-1).bit_length()

        res = lst[:]
        for i in range(n):
            j = 0
            for k in range(num):
                j |= ((i >> k) & 1) << (num - 1 - k)
            if (i < j):
                res[i], res[j] = res[j], res[i]

        for i in range(num):
            i = (1 << i)
            for j in range(i):
                x = (2*inv - 1) * (2*PI*j) / (2*i)
                w = complex(cos(x), sin(x))
                for k in range(0, n, i*2):
                    s, t = res[j+k], res[i+j+k] * w
                    res[j+k], res[i+j+k] = s+t, s-t
        if (inv):
            res = [ri / n for ri in res]
        return res

    len_ab = len(a) + len(b) - 1
    n = 1 << len_ab.bit_length()

    a += [0] * (n-len(a))
    b += [0] * (n-len(b))

    res = [ai * bi for ai, bi in zip(FFT(a), FFT(b))]
    res = [int(fi.real + 0.1) for fi in FFT(res, True)[:len_ab]]
    return res


# 畳み込み(MOD)
def convolve_MOD(a, b):
    mod = 998244353
    g, e = pow(3, 119, mod), 24
    ginv = pow(g, mod-2, mod)
    # 998244353 = 119 * 2**23 + 1

    # 高速剰余変換 O(nlogn)
    def FMT(lst, inv=False):
        res = lst[:]
        for i in range(n):
            j = 0
            for k in range(n_lenbit):
                j |= ((i >> k) & 1) << (n_lenbit - 1 - k)
            if (i < j):
                res[i], res[j] = res[j], res[i]

        for i in range(n_lenbit):
            w =1
            wp = Winv[e-2-i] if inv else W[e-2-i]
            pow2i = (1 << i)
            
            for j in range(pow2i):
                for k in range(1 << (n_lenbit-i-1)):
                    idx = k * pow2i*2 + j
                    s, t = res[idx], res[idx + pow2i] * w
                    res[idx], res[idx + pow2i] = (s + t) % mod, (s - t) % mod
                w = (w * wp) % mod

        if (inv):
            n_inv = pow(n, mod-2, mod)
            res = [ri * n_inv % mod for ri in res]
        return res


    W, Winv = [g], [ginv]
    for _ in range(e):
        W.append(W[-1]**2 % mod)
        Winv.append(Winv[-1]**2 % mod)
    len_ab = len(a) + len(b) - 1
    n = 1 << len_ab.bit_length()
    n_lenbit = (n-1).bit_length()
    a += [0] * (n-len(a))
    b += [0] * (n-len(b))

    res = [ai * bi % mod for ai, bi in zip(FMT(a), FMT(b))]
    res = FMT(res, inv=True)[:len_ab]
    return res
