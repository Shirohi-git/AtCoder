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


# 天井関数 ceil(X/Y) (Y>1)
def ceil(x, y):
    return (x + y - 1) // y


# 高精度 X**0.5
def int_sqrt(num):
    res = int(num**0.5)-1
    while (res+1)**2 <= num:
        res += 1
    return res


# 最小公倍数
def lcm(X, Y):
    from math import gcd
    return (X * Y) // gcd(X, Y)


# 有理数クラス(y/x)
def quotient(x, y):
    from math import gcd
    if x == y == 0:
        return (0, 0)
    if (y < 0) or (y == 0 and x < 0):
        x, y = -x, -y
    t = gcd(x, y)
    return (x//t, y//t)


# 拡張互除法 output: z, x, y subject to: ax + by = z
# where z = gcd(a, b)
def extgcd(a, b):
    is_mn_a, is_mn_b = 0, 0
    if a < 0:
        a, is_mn_a = abs(a), 1
    if b < 0:
        b, is_mn_b = abs(b), 1

    x, y, u, v = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x, u = u, x - q * u
        y, v = v, y - q * v

    x -= 2 * is_mn_a * x
    y -= 2 * is_mn_b * y
    return a, x, y


# 中国剰余定理
def crt(num_mod):
    res, mod = num_mod[0]
    for ai, mi in num_mod:
        g, x, y = extgcd(mod, mi)
        if (res - ai) % g:
            return 0, -1
        mod = mod * mi // g
        div = (res - ai) // g
        res = (div * y * mi + ai) % mod
    return res, mod


# 素因数分解 O(X**0.5)
def factorize(n0):
    p, res = 2, []
    while p * p <= n0:
        while n0 % p == 0:
            n0 //= p
            res.append(p)
        p += 1
    if n0 > 1:
        res.append(n0)
    return res


# 約数列挙 O(X**0.5)
def makedivisor(n0):
    p, upper, lower = 1, [], []
    while p * p <= n0:
        if n0 % p == 0:
            lower.append(p)
            if p * p != n0:
                upper.append(n0 // p)
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


# 立ってるbitの数リスト O(2**N)
def bitcount(n0):
    bitcnt = [0]
    for _ in range(n0):
        bitcnt += [i + 1 for i in bitcnt]
    return bitcnt


# bitの部分集合 sum(0~2^N) = O(3^N)
def bitsubset(n0):
    ini = n0
    res = [n0]
    while n0 > 0:
        n0 = (n0-1) & ini
        res.append(n0)
    return res


# 数え上げなど # N<=10**6
class Enumeration:
    # 前処理(各i の 階乗, 逆元, 階乗の逆元)
    def __init__(self, N, MOD):
        self.mod = MOD
        self.FACT = [1, 1]
        self.INV = [0, 1]
        self.FACTINV = [1, 1]
        for i in range(2, N + 1):
            self.FACT.append((self.FACT[-1] * i) % self.mod)
            self.INV.append(pow(i, self.mod - 2, self.mod))
            self.FACTINV.append((self.FACTINV[-1] * self.INV[-1]) % self.mod)

    # nCr(mod p)
    def combination(self, N, R):
        if (R < 0) or (N < R):
            return 0
        R = min(R, N - R)
        div = self.FACTINV[R] * self.FACTINV[N-R] % self.mod
        return self.FACT[N] * div % self.mod


# nCr(mod p) #n>=10**7,r<=10**6 #前処理不要
def bigcmb(N, R, MOD):
    if (R < 0) or (N < R):
        return 0
    R = min(R, N - R)
    fact, inv = 1, 1
    for i in range(1, R + 1):
        fact = (fact * (N - i + 1)) % MOD
        inv = (inv * i) % MOD
    return fact * pow(inv, MOD - 2, MOD) % MOD


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


# 偏角ソート
def arg_sort(points, ymax=10**20):

    def sub_sort(sub_p):
        if (not sub_p) or (sub_p[0][0] == 0):
            return sub_p
        res = sorted(sub_p, key=lambda p: p[1] * ymax // p[0])
        return res

    group = [[], [], [], [], []]
    for xi, yi in points:
        if yi < 0:
            group[2 + (xi >= 0) + (xi > 0)].append((xi, yi))
        elif yi >= 0:
            group[(xi <= 0) + (xi < 0)].append((xi, yi))

    res = sum([sub_sort(gi) for gi in group], [])
    return res


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
def convolve(x, y):

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

    a, b = x[:], y[:]
    len_ab = len(a) + len(b) - 1
    n = 1 << len_ab.bit_length()
    a += [0] * (n-len(a))
    b += [0] * (n-len(b))

    res = [ai * bi for ai, bi in zip(FFT(a), FFT(b))]
    res = [int(fi.real + 0.1) for fi in FFT(res, True)[:len_ab]]
    return res


# 畳み込み(MOD)
class Convolve_MOD:
    def __init__(self):
        self.mod = mod = 998244353
        self.g, self.e = g, e = pow(3, 119, mod), 24
        self.ginv = ginv = pow(g, mod-2, mod)

        self.W, self.Winv = [g], [ginv]
        for _ in range(e):
            self.W.append(self.W[-1]**2 % mod)
            self.Winv.append(self.Winv[-1]**2 % mod)

    # 高速剰余変換 O(nlogn)
    def FMT(self, lst, inv=False):
        res = lst[:]
        for i in range(self.n):
            j = 0
            for k in range(self.n_lenbit):
                j |= ((i >> k) & 1) << (self.n_lenbit - 1 - k)
            if (i < j):
                res[i], res[j] = res[j], res[i]

        for i in range(self.n_lenbit):
            w, wp = 1, self.W[self.e - 2 - i]
            if inv:
                wp = self.Winv[self.e - 2 - i]
            pow2i = (1 << i)

            for j in range(pow2i):
                for k in range(1 << (self.n_lenbit - i-1)):
                    idx = k * pow2i*2 + j
                    s, t = res[idx], res[idx + pow2i] * w
                    res[idx] = (s + t) % self.mod
                    res[idx + pow2i] = (s - t) % self.mod
                w = (w * wp) % self.mod

        if (inv):
            n_inv = pow(self.n, self.mod-2, self.mod)
            res = [ri * n_inv % self.mod for ri in res]
        return res

    def convolve(self, x, y):
        a, b = x[:], y[:]
        len_ab = len(a) + len(b) - 1
        self.n = n = 1 << len_ab.bit_length()
        self.n_lenbit = (n-1).bit_length()
        a += [0] * (n-len(a))
        b += [0] * (n-len(b))

        res = [ai * bi % self.mod for ai, bi in zip(self.FMT(a), self.FMT(b))]
        res = self.FMT(res, inv=True)[:len_ab]
        return res
