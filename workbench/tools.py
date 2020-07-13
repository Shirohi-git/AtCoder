# pypyは内包表記NG,再帰NG,dict.key()NG

# floatを使うときは大きい数に注意
# in dict.values() はO(n)

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


def ceil(X, Y):  # 天井関数 ceil(X/Y) Y!=1
    return (X + Y - 1) // Y


def lcm(X, Y):  # 最小公倍数
    from math import gcd
    return (X * Y) // gcd(X, Y)


def factorize(N):
    p = 2
    PRIME = []
    while p * p <= N:
        if N % p == 0:
            N //= p
            PRIME.append(p)
        else:
            p += 1
    if N > 1:
        PRIME.append(N)
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


def nearlist(N,LIST):# 隣接リスト
    NEAR = [[] for _ in range(N)]
    for a, b in LIST:
        NEAR[a - 1].append(b - 1)
        NEAR[b - 1].append(a - 1)
    return NEAR


def bfs(NEAR, S, N):  # 幅優先探索  # キュー
    # 隣点リスト,始点,数
    from collections import deque

    dist = [-1 for _ in range(N)]  # 前処理
    pas = [-1 for _ in range(N)]
    dist[S], pas[S] = 0, 's'
    que, frag = deque([S]), set([S])

    while len(que) > 0:
        q = que.popleft()
        for i in NEAR[q]:  # 移動先の候補
            if i in frag:  # 処理済みか否か
                continue
            # 処理を行う
            que.append(i), frag.add(i)
    return


def dfs(NEAR, S, N):  # 深優先探索  # スタック
    # 隣点リスト,始点,数

    dist = [-1 for _ in range(N)]  # 前処理
    pas = [-1 for _ in range(N)]
    dist[S], pas[S] = 0, 's'
    stack, frag = [S], set([S])

    while len(stack) > 0:
        q = stack.pop()
        for i in NEAR[q]:  # 移動先の候補
            if i in frag:  # 処理済みか否か
                continue
            # 処理を行う
            stack.append(i), frag.add(i)
    return


class Recursive_dfs():  # 深優先探索(再帰)  # スタック
    # 隣点リスト,始点,数
    
    def __init__(self, NEAR, S, N):
        # 前処理
        self.frag = set([S])
        self.near = NEAR

    def recdfs(self, p):
        for i in self.near[p]:  # 移動先の候補
            if i in self.frag:  # 処理済みか否か
                continue
            # 処理を行う
            self.frag.add(i)
            self.recdfs(i)


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


class Unionfind():  # Unionfind
    def __init__(self, N):
        self.N = N
        self.parents = [-1] * N

    def find(self, x):  # グループの根
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):  # グループの併合
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):  # グループのサイズ
        return -self.parents[self.find(x)]

    def same(self, x, y):  # 同じグループか否か
        return self.find(x) == self.find(y)

    def members(self, x):  # グループの要素
        root = self.find(x)
        return [i for i in range(self.N) if self.find(i) == root]

    def roots(self):  # 根のリスト
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):  # グループの数
        return len(self.roots())

    def all_group_members(self):  # グループごとの辞書
        return {r: self.members(r) for r in self.roots()}


class Segtree():  # Segtree

    def segfunc(self, x, y):  # 区間にしたい操作
        return max(x, y)  # ex) max,min,gcd,lcm,sum,product

    def __init__(self, LIST, ide_ele):  # LIST: 配列の初期値, ide_ele: 単位元
        n = len(LIST)
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
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
