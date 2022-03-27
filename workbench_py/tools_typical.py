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
def inversion_number(n0, lst0):
    res = 0
    bit = Fenwicktree(n0)
    for li in lst0:
        bit.update(li, 1)
        res += bit.query(li+1, n0)
    return res


# 最長部分増加列 長さidxの最小の数を保存 O(NlogN)
def LIS(lst0):
    from bisect import bisect_left

    dp = []
    for ai in lst0:
        idx = bisect_left(dp, ai)
        if len(dp) <= idx:
            dp.append(ai)
        dp[idx] = ai
    return len(dp)


# TSP or ハミルトン経路 lst0:隣接行列 O(N**2 * 2**N)
def tsp_hamilton(n0, lst0, inf=10**10, tsp=True):
    dist = [[inf] * n0 for _ in range(2**n0)]
    dist[1 << 0][0] = 0
    que = [(1 << 0, 0)]
    if not tsp:
        for i in range(n0):
            dist[1 << i][i] = 0
        que = [(1 << i, i) for i in range(n0)]

    for bit, q in que:
        for i in range(n0):
            if (bit >> i) & 1:
                continue
            nxt = bit | (1 << i)
            if lst0[q][i] > 0:
                d_nqi = dist[bit][q] + lst0[q][i]
                if dist[nxt][i] == inf:
                    dist[nxt][i] = d_nqi
                    que.append((nxt, i))
                dist[nxt][i] = min(dist[nxt][i], d_nqi)

    if tsp:
        goal = [inf] * n0
        for i, d in enumerate(dist[-1]):
            goal[i] = d + lst0[i][0]
        dist.append(goal)
    return min(dist[-1])
