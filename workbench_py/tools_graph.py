# 隣接リスト
def nearlist(n0, lst0):
    res = [[] for _ in range(n0)]
    for a, b in lst0:
        res[a-1].append(b-1)
        res[b-1].append(a-1)
    return res


# 重み付き隣接リスト
def weighted_nearlist(n0, lst0):
    res = [set() for _ in range(n0)]
    for a, b, w in lst0:
        res[a-1].add((b-1, w))
    return res


# 幅優先探索 # 始点, 頂点数, 隣接リスト
def bfs(s0, n0, near0):
    dist = [-1] * n0
    path = [-1] * n0
    flag = [0] * n0
    dist[s0], path[s0] = 0, 's'
    flag[s0] = 1
    que = [s0]

    for q in que:
        for i in near0[q]:
            if flag[i]:
                continue
            flag[i] = 1
            que.append(i)
    return


# que幅優先探索 # 始点, 頂点数, 隣接リスト
def que_bfs(s0, n0, near0):
    from collections import deque

    dist = [-1] * n0
    path = [-1] * n0
    flag = [0] * n0
    dist[s0], path[s0] = 0, 's'
    flag[s0] = 1
    que = deque([s0])

    while que:
        q = que.popleft()
        for i in near0[q]:
            if flag[i]:
                continue
            flag[i] = 1
            que.append(i)
    return


# grid幅優先探索 # 始点, 縦, 横
def grid_bfs(s0, h0, w0):
    from collections import deque

    sx, sy = s0
    dist = [[-1] * w0 for _ in range(h0)]
    path = [[-1] * w0 for _ in range(h0)]
    flag = [[0] * w0 for _ in range(h0)]
    dist[sx][sy], path[sx][sy], flag[sx][sy] = 0, 's', 1
    que = deque([s0])

    near = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while que:
        qx, qy = que.popleft()
        for dx, dy in near:
            px, py = qx+dx, qy+dy
            if 0 <= px < h0 and 0 <= py < w0:
                if flag[px][py]:
                    continue
                flag[px][py] = 1
                que.append((px, py))
    return


# 深優先探索  # スタック # 始点, 頂点数, 隣接リスト
def dfs(s0, n0, near0):
    dist = [-1] * n0
    path = [-1] * n0
    flag = [0] * n0
    dist[s0], path[s0] = 0, 's'
    flag[s0] = 1
    stack = [s0]

    while stack:
        q = stack.pop()
        for i in near0[q]:
            if flag[i]:
                continue
            flag[i] = 1
            stack.append(i)
    return


# 深優先探索(帰り)
def back_dfs(s0, n0, near0):
    dist = [-1] * n0
    path = [-1] * n0
    flag = [0] * n0
    dist[s0], path[s0] = 0, 's'
    flag[s0] = 1
    stack = [s0]
    near_it = [iter(ni) for ni in near0]

    while stack:
        q = stack[-1]
        for i in near_it[q]:
            if flag[i]:
                continue
            flag[i] = 1
            stack.append(i)
            break
        else:
            stack.pop()
    return


# 二部グラフ判定 # 始点, 頂点数, 隣接リスト
def is_bipartite(s, n0, near0):
    color = [0 for _ in range(n0)]
    color[s] = 1
    stack = [(s, 1)]

    while stack:
        q, c = stack.pop()
        for i in near0[q]:
            if color[i] == c:
                return False
            if color[i] == 0:
                color[i] = -c
                stack.append((i, -c))
    return True


# ダイクストラ法:単一始点最短経路 O((V+E)*logV) # near0:隣接リスト
def dijkstra(s0, n0, near0, inf=10**18):
    from heapq import heappop, heappush
    DIST, prev = [inf] * n0, [-1] * n0
    DIST[s0], prev[s0] = 0, 's'

    que = [(DIST[s0], s0)]
    while que:
        d, q = heappop(que)
        if DIST[q] < d:
            continue
        for i, d_qi in near0[q]:
            tmp = d + d_qi
            if DIST[i] > tmp:
                DIST[i] = tmp
                prev[i] = q
                heappush(que, (tmp, i))
    return DIST


# ベルマンフォード法:単一始点最短経路(負閉路有) O(VE) # edge0:辺リスト
def bellmanford(s0, n0, edge0, inf=10**18):
    res = [inf] * n0
    res[s0] = 0

    for i in range(n0 * 2):
        for a, b, d in edge0:
            if res[a-1] + d < res[b-1]:
                res[b-1] = (res[a-1] + d if i < n0 else -inf)
    return res


# ワーシャルフロイド法:全頂点対最短経路 O(V**3) # lst0:隣接行列
def warshallfloyd(n0, lst0):
    res = [li[:] for li in lst0]
    for k in range(n0):
        for i in range(n0):
            for j in range(n0):
                res[i][j] = min(res[i][j], res[i][k] + res[k][j])
    return res


# トポロジカルソート:DAGに適用可, edge0:有向辺リスト
def topological(N, edge0):
    from collections import deque

    incnt = [0] * N
    child = [set() for _ in range(N)]
    for a, b in edge0:
        child[a - 1].add(b - 1)
        incnt[b - 1] += 1

    tprg = []
    que = deque([i for i, num in enumerate(incnt) if num == 0])
    while que:
        q = que.popleft()
        for i in child[q]:
            incnt[i] -= 1
            if incnt[i] == 0:
                que.append(i)
        tprg.append(q)
    return tprg


# プリム法:最小全域木
def prim(n0, near0):
    from heapq import heappush, heappop, heapify

    flag = [0] * n0
    flag[0] = 1
    que = [(c, j, 0) for j, c in near0[0]]
    heapify(que)

    ans = []
    while que:
        c_pq, q, p = heappop(que)
        if flag[q]:
            continue
        flag[q] = 1
        ans.append((p, q, c_pq))
        for r, c_qr in near0[q]:
            if 1 - flag[r]:
                heappush(que, (c_qr, r, q))
    return ans


# クラスカル法:最小全域木, UF木が必要
def kruskal(k_uf, near0):
    edge = []
    for i, ni in enumerate(near0):
        edge += [(c, i, j) for j, c in ni if i < j]
    edge = sorted(edge)

    res = 0
    for w, i, j in edge:
        if not k_uf.same(i, j):
            res += w
            k_uf.unite(i, j)
    return res


# Unionfind
class Unionfind:
    # find:グループの根, unite:グループの併合, same:同じグループか否か
    def __init__(self, n0):
        self.n = n0
        self.len = n0
        self.parents = [-1] * n0

    def find(self, x):
        stack = []
        while self.parents[x] >= 0:
            stack.append(x)
            x = self.parents[x]
        for i in stack:
            self.parents[i] = x
        return x

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.len -= 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    # roots:根のリスト
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    # size:特定のグループのサイズ, all_sizes:全てのグループのサイズ
    def size(self, x):
        return - self.parents[self.find(x)]

    def all_sizes(self):
        return {i: -x for i, x in enumerate(self.parents) if x < 0}

    # member:特定のグループの要素, all_members:全てのグループごとの要素
    def member(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def all_members(self):
        group = {i:[] for i, x in enumerate(self.parents) if x < 0}
        for i in range(self.n):
            group[self.find(i)].append(i)
        return group


# 強連結成分分解
class Strongly_Conected_Component:

    # near0:有向辺隣接リスト, rv_near: 逆向き枝, order: 帰りがけ順
    def __init__(self, n0, near0):
        self.n = n0
        self.near = [ni[:] for ni in near0]
        self.nm_near = [iter(ni) for ni in near0]
        self.rv_near = [[] for _ in range(self.n)]
        for i in range(self.n):
            for j in near0[i]:
                self.rv_near[j].append(i)

        self.flag_dfs = [0] * self.n
        self.order = []
        for i in range(self.n):
            if not self.flag_dfs[i]:
                self.dfs(i)

        self.cnt = 0
        self.flag_rdfs = [0] * self.n
        self.idx = [-1] * self.n
        for i in self.order[::-1]:
            if not self.flag_rdfs[i]:
                self.rdfs(i)
                self.cnt += 1

        self.grp_v = [[] for _ in range(self.cnt)]
        for i in range(self.n):
            self.grp_v[self.idx[i]].append(i)
        return

    def dfs(self, v):
        self.flag_dfs[v] = 1
        stack = [v]

        while stack:
            now = stack[-1]
            for nxt in self.nm_near[now]:
                if not self.flag_dfs[nxt]:
                    self.flag_dfs[nxt] = 1
                    stack.append(nxt)
                    break
            else:
                stack.pop()
                self.order.append(now)
        return

    def rdfs(self, v):
        self.idx[v] = self.cnt
        stack = [v]

        while stack:
            now = stack.pop()
            if self.flag_rdfs[now]:
                continue
            self.flag_rdfs[now] = 1
            for nxt in self.rv_near[now]:
                if not self.flag_rdfs[nxt]:
                    self.idx[nxt] = self.cnt
                    stack.append(nxt)
        return

    # グラフ縮約
    def construct(self):
        graph = [set() for _ in range(self.cnt)]
        for v in range(self.n):
            v_id = self.idx[v]
            for w in self.near[v]:
                w_id = self.idx[w]
                if v_id != w_id:
                    graph[v_id].add(w_id)
        return graph


# Dinic法:最大流問題, 最小カット問題 O(m n^2) など 
# https://misawa.github.io/others/flow/dinic_time_complexity.html
class Dinic:
    def __init__(self, n0):
        self.N, self.INF = n0, 10**10
        self.edge_cnt = 0
        self.edge = []
        self.near_edge = [[] for _ in range(n0)]

    # 順向き枝:偶数, 逆向き枝:奇数
    def add__edge(self, v1, v2, cap1, cap2=0):
        self.edge += [[v2, cap1], [v1, cap2]]
        self.near_edge[v1].append(self.edge_cnt)
        self.near_edge[v2].append(self.edge_cnt + 1)
        self.edge_cnt += 2

    # 残余グラフでの接続判定+ランク付(BFS)
    def is_connect(self, s, t):
        self.level = level = [-1] * self.N
        que = [s]
        level[s] = 0

        for v in que:
            for e_idx in self.near_edge[v]:
                w, cap = self.edge[e_idx]
                if cap and level[w] < 0:
                    level[w] = level[v] + 1
                    que.append(w)
        return (level[t] >= 0)

    # 残余グラフで流せるだけ流す(DFS) # s==tで壊れる
    def add_flow(self, s, t):
        goal = 0
        edge = self.edge
        stack = [(s, self.INF, -1)]
        while stack:
            v, bfo_cap, bfo_idx = stack[-1]

            if v == t:
                goal, res = 1, bfo_cap

            if goal:
                if v == s:
                    return res
                edge[bfo_idx][1] -= res
                edge[bfo_idx ^ 1][1] += res
                stack.pop()
                continue

            for e_idx in self.ne_iter[v]:
                w, cap = edge[e_idx]
                if cap and self.level[v] < self.level[w]:
                    stack.append((w, min(bfo_cap, cap), e_idx))
                    break
            else:
                stack.pop()
        return 0

    # s==tで壊れる
    def flow(self, s, t):
        flow = 0
        while self.is_connect(s, t):
            self.ne_iter = list(map(iter, self.near_edge))
            f = self.INF
            while f:
                f = self.add_flow(s, t)
                flow += f
        return flow
