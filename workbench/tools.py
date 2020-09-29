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
# フェルマーの小定理(mは素数, kはmと互いに素)
# pow(a, mod-1, mod) == 1 (mod_p) <=> pow(a, mod-2, mod) == a**(-1) (mod_p)
# 割り算するところを掛け算できるので先にmodが取れる


def ceil(X, Y):  # 天井関数 ceil(X/Y) Y>1
    return (X + Y - 1) // Y


def lcm(X, Y):  # 最小公倍数
    from math import gcd
    return (X * Y) // gcd(X, Y)


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


class Eratosthenes():  # エラトステネスの篩
    def __init__(self, N):  # 素数リスト生成 O(n*log(log n))
        self.fact = [i for i in range(N + 1)]
        for i in range(2, int(N ** 0.5) + 1):
            if self.fact[i] < i:
                continue
            for j in range(i ** 2, N + 1, i):
                self.fact[j] = i
        self.prime = [i for i in range(2, N + 1) if i == self.fact[i]]

    def factor(self, NUM):  # 高速素因数分解 O(log num)
        PRIME = set()
        while NUM > 1:
            PRIME.add(self.fact[NUM])
            NUM //= self.fact[NUM]
        return PRIME


class Combination():  # nCr(mod p) #n<=10**6
    def __init__(self, N, MOD):  # cmbの前処理
        self.mod = MOD
        self.FACT = [1, 1]  # 階乗
        self.INV = [0, 1]  # 各iの逆元
        self.FACTINV = [1, 1]  # 階乗の逆元
        for i in range(2, N + 1):
            self.FACT.append((self.FACT[-1] * i) % self.mod)
            self.INV.append(pow(i, self.mod - 2, self.mod))
            self.FACTINV.append((self.FACTINV[-1] * self.INV[-1]) % self.mod)

    def count(self, N, R):  # nCr(mod p) #前処理必要
        if (R < 0) or (N < R):
            return 0
        R = min(R, N - R)
        return self.FACT[N] * self.FACTINV[R] * self.FACTINV[N-R] % self.mod


def bigcmb(N, R, MOD):  # nCr(mod p) #n>=10**7,r<=10**6 #前処理不要
    if (R < 0) or (N < R):
        return 0
    R = min(R, N - R)
    fact, inv = 1, 1
    for i in range(1, R + 1):
        fact = (fact * (N - i + 1)) % MOD
        inv = (inv * i) % MOD
    return fact * pow(inv, MOD - 2, MOD) % MOD


def bitcount(N):  # 立ってるbitの数
    bitcnt = [0]
    for _ in range(N):
        bitcnt += [i + 1 for i in bitcnt]
    return bitcnt


def binary(N):  # 二分探索 # N:探索要素数
    l, r = -1, N
    while r - l > 1:
        if True:  # 条件式を代入
            r = (l + r) // 2
        else:
            l = (l + r) // 2
    return r + 1


def knapsack(N, W, ITEM):  # ナップザック問題 # 典型dp
    # 個数,上限重さ,itemリスト
    dp = [[0] + [0] * W] + [[-float("inf")] * (W + 1) for _ in range(N)]
    # dp初期値 必要に応じて変える
    #dp = [[0] + [-float("inf")]*w] + [[-float("inf")]*(w+1) for _ in range(n)]
    # 重さwぴったり、を求めるとき
    wei, val = 0, 1

    for i in range(N):  # i個目までのitemについて
        for j in range(W+1):  # 重さjまでの最適総価値
            if ITEM[i][wei] <= j:
                dp[i + 1][j] = max(dp[i][j],
                                   dp[i][j-ITEM[i][wei]] + ITEM[i][val])
            else:
                dp[i + 1][j] = dp[i][j]
    return dp[N][W]


def lcs(S, T):  # 最長共通部分列 # s,t:文字列
    ls, lt = len(S), len(T)
    dp = [[0] * (lt + 1) for _ in range(ls + 1)]
    dp[0][0], dp[1][0], dp[0][1] = 0, 0, 0
    for i in range(ls):
        for j in range(lt):
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
            if S[i] == T[j]:
                dp[i + 1][j + 1] = max(dp[i][j] + 1, dp[i + 1][j + 1])
    return dp[ls][lt]


def memodp(DP, NEAR, x):
    if True:  # 条件式
        return DP[x]
    else:
        for i in NEAR[x]:
            DP[x] += memodp(DP, NEAR, i)
            # 漸化式
        return DP[x]


class Segtree():  # Segtree

    def segfunc(self, x, y):  # 区間にしたい操作
        return max(x, y)  # ex) max,min,gcd,lcm,sum,product

    def __init__(self, LIST, ELE):  # LIST: 配列の初期値, ELE: 単位元
        n, self.ide_ele = len(LIST), ELE
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ELE] * 2 * self.num
        for i in range(n):  # 配列の値を葉にセット
            self.tree[self.num + i] = LIST[i]
        for i in range(self.num - 1, 0, -1):  # 構築していく
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
