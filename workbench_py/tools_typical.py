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


# 三分探索
def ternary(ok, ng):
    # 下凸な関数
    def func(x):
        return x**2

    def is_OK(m1, m2):
        return func(m1) >= func(m2)

    while abs(ng - ok) > 2:
        mid1 = (2 * ok + ng) // 3
        mid2 = (ok + 2 * ng) // 3

        if is_OK(mid1, mid2):
            ok = mid1
        else:
            ng = mid2
    return ok, ng


# ナップザック問題 # 典型dp
def knapsack(n0, w0, ITEM, inf=10**18):
    # 個数,上限重さ,itemリスト
    dp = [[0] * (w0 + 1)] + [[-inf] * (w0 + 1) for _ in range(n0)]
    # dp = [[-inf] * (w0+1)] + [[-inf] * (w0+1) for _ in range(n0)]
    # dp[0][0] = 0
    # 重さwぴったり、を求めるとき
    wei, val = 0, 1

    for i in range(n0):
        for j in range(w0 + 1):
            tmp = dp[i][j]
            if ITEM[i][wei] <= j:
                tmp = dp[i][j - ITEM[i][wei]] + ITEM[i][val]
            dp[i + 1][j] = max(dp[i][j], tmp)
    return dp[n0][w0]


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
def TSP_hamilton(n0, lst0, inf=10**10, tsp=True):
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


# 最小共通祖先(SparseTable(min))
class LCA():
    def __init__(self, n0, edge, inf=10**7):
        near = self.nearlist(n0, edge)
        order = self.back_dfs(0, n0, near)
        self.idx = [-1] * n0
        for i, (_, v) in [*enumerate(order)][::-1]:
            self.idx[v] = i
        self.spt = SparseTable(order, (inf, inf))
        return

    def nearlist(self, n0, lst0):
        res = [[] for _ in range(n0)]
        for a, b in lst0:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        return res

    def back_dfs(self, s0, n0, near0):
        dist = [-1] * n0
        dist[s0] = 0
        stack = [s0]
        near_it = [iter(ni) for ni in near0]

        res = []
        while stack:
            q = stack[-1]
            res.append((dist[q], q))
            for i in near_it[q]:
                if dist[i] > -1:
                    continue
                dist[i] = dist[q] + 1
                stack.append(i)
                break
            else:
                stack.pop()
        return res

    def query(self, s, t):
        l, r = self.idx[s-1], self.idx[t-1]
        if l > r:
            l, r = r, l
        depth, idx = self.spt.query(l, r+1)
        return idx+1
