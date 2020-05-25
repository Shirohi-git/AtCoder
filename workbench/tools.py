# pypyは内包表記,再帰NG,dict.key()がゴミほど遅い

# floatを使うときは大きい数に注意

# 入力が多い時
import sys
input = sys.stdin.readline

# 再帰の深さに注意
sys.setrecursionlimit(10 ** 7)

# 冪乗 n ** m % mod == pow(n, m, mod)
# フェルマーの小定理(mは素数, kはmと互いに素)
# pow(a, mod-1, mod) == 1 (mod_p) <=> pow(a, mod-2, mod) == a**(-1) (mod_p)
# 割り算するところを掛け算できるので先にmodが取れる


def lcm(X, Y):  # 最小公倍数
    import math
    return (X * Y) // math.gcd(X, Y)


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


def pre_cmb(N, MOD):  # cmbの前準備 #順列諸々にも使えそう
    FACT = [1, 1]  # 階乗
    INV = [0, 1]  # 各iの逆元
    FACTINV = [1, 1]  # 階乗の逆元

    for i in range(2, N + 1):
        FACT.append((FACT[-1] * i) % MOD)
        INV.append(pow(i, MOD-2, MOD))
        FACTINV.append((FACTINV[-1] * INV[-1]) % MOD)
    PRELIST = FACT, FACTINV
    return PRELIST


def cmbcount(N, R, MOD, PRELIST):  # nCr(mod p)
    FACT, FACTINV = PRELIST
    if (R < 0) or (N < R):
        return 0
    R = min(R, N - R)
    return FACT[N] * FACTINV[R] * FACTINV[N-R] % MOD


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


def bfs(NEAR, S, N):  # 幅優先探索  # キュー
    # 隣点リスト,始点,数
    from collections import deque

    dist = [-1 for _ in range(N)]  # 前処理
    pas = [-1 for _ in range(N)]
    dist[S], pas[S] = 0, 's'
    frag = set([S])
    que = deque([S])

    while len(que) > 0:
        q = que.popleft()
        for i in NEAR[q]:  # 移動先の候補
            if i in frag:  # 処理済みか否か
                continue
            # 処理を行う
            que.append(i)
            frag.add(i)
    return


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


def longdist(P, dp_l, out_l):  # メモ化再帰,再帰部分
    # dp_l=dp:list out_l=output:list
    if len(out_l[P]) == 0:
        return 0
    for q in out_l[P]:
        if dp_l[q] == -1:
            dp_l[q] = longdist(q, dp_l, out_l)
        dp_l[P] = max(dp_l[P], dp_l[q]+1)
    return dp_l[P]


def longestdist(N, XY):  # 有向グラフ最長路長 # メモ化再帰
    input, output = [[] for _ in range(N)], [[] for _ in range(N)]
    for x, y in XY:
        input[y - 1].append(x - 1)
        output[x - 1].append(y - 1)
    dp = [-1] * N
    for i in range(N):
        if dp[i] == -1:
            dp[i] = longdist(i, dp, output)
    return max(dp)
