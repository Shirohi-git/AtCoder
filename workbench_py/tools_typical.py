from tools_graph import*
from tools_math import*
from tools_string import*
from tools_structure import*


# 二分探索
def binary(ok, ng):
    def is_OK():
        return True

    while abs(ng - ok) > 1:
        mid = (ok + ng) // 2
        if is_OK(mid):
            ok = mid
        else:
            ng = mid
    return ok


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


# 転倒数 O(NlogN)
def inversion_number(n0, lst):
    res = 0
    bit = Fenwicktree(n0)
    for li in lst:
        bit.update(li, 1)
        res += bit.query(li+1, n0)
    return res


# 最長部分増加列 長さidxの最小の数を保存
def LIS(L):
    from bisect import bisect_left

    dp = []
    for ai in L:
        idx = bisect_left(dp, ai)
        if len(dp) <= idx:
            dp.append(ai)
        dp[idx] = ai
    return len(dp)


# 巡回セールスマン問題
class TSP():
    def __init__(self, n):
        self.n = n
        self.memo = [[-1] * (1 << n) for _ in range(n)]
        self.dist = [[0] * n for _ in range(n)]
        # 頂点間の距離の入力

    # s: 次訪問地, bit: 未訪問=1   # どうして...こうなった...
    def tspdp(self, s=0, bit=1):
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
