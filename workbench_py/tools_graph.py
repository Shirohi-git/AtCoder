def nearlist(N, LIST):  # 隣接リスト
    NEAR = [set() for _ in range(N)]
    for a, b in LIST:
        NEAR[a - 1].add(b - 1)
        NEAR[b - 1].add(a - 1)
    return NEAR


def weighted_nearlist(N, LIST):  # 重み付き隣接リスト
    NEAR = [set() for _ in range(N)]
    for a, b, w in LIST:
        NEAR[a - 1].add((b - 1, w))
    return NEAR


def bfs(S, N, NEAR):  # 幅優先探索  # キュー
    # 始点, 頂点数, 隣接リスト
    from collections import deque

    dist = [-1] * N  # 前処理
    path = [-1] * N
    flag = [0] * N
    dist[S], path[S] = 0, 's'
    flag[S] = 1
    que = deque([S])

    while que:
        q = que.popleft()
        for i in NEAR[q]:  # 移動先の候補
            if flag[i]:  # 処理済みか否か
                continue
            # 処理を行う
            flag[i] = 1
            que.append(i)
    return


def dfs(S, N, NEAR):  # 深優先探索  # スタック
    # 始点, 頂点数, 隣接リスト
    dist = [-1] * N  # 前処理
    path = [-1] * N
    flag = [0] * N
    dist[S], path[S] = 0, 's'
    flag[S] = 1
    stack = [S]

    while stack:
        q = stack.pop()
        for i in NEAR[q]:  # 移動先の候補
            if flag[i]:  # 処理済みか否か
                continue
            # 処理を行う
            flag[i] = 1
            stack.append(i)
    return


class Recursive_dfs():  # 深優先探索(再帰)
    import sys
    sys.setrecursionlimit(10 ** 7)

    def __init__(self, S, N, NEAR):
        # 始点, 頂点数, 隣接リスト
        self.flag = [0] * N  # 前処理
        self.flag[S] = 1
        self.near = NEAR

    def recdfs(self, p):
        for i in self.near[p]:  # 移動先の候補
            if self.flag[i]:  # 処理済みか否か
                continue
            # 処理を行う
            self.flag[i] = 1
            self.recdfs(i)


def is_bipartite(S, N, NEAR):  # 二部グラフ判定
    # 始点, 頂点数, 隣接リスト
    color = [0 for i in range(N)]
    stack = [(S, 1)]
    while stack:
        q, c = stack.pop()
        for i in NEAR[q]:
            if color[i] == c:
                return False
            if color[i] == 0:
                color[i] = -c
                stack.append((i, -c))
    return True


def dijkstra(S, N, NEAR):  # ダイクストラ法:単一始点最短経路 O((n+e)*logn)
    # NEAR:隣接リスト
    from heapq import heappop, heappush
    DIST, prev = [pow(10, 10)] * N, [-1] * N
    DIST[S], prev[S] = 0, 's'

    que = [(DIST[S], S)]
    while que:
        d, q = heappop(que)
        if DIST[q] < d:
            continue
        for i, d_qi in NEAR[q]:
            tmp = d + d_qi
            if DIST[i] > tmp:
                DIST[i] = tmp
                prev[i] = q
                heappush(que, (tmp, i))
    return DIST


def warshallfloyd(N, LIST):  # ワーシャルフロイド法:全頂点対最短経路 O(n**3)
    # LIST:隣接行列
    from copy import deepcopy
    DIST = deepcopy(LIST)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                DIST[i][j] = min(DIST[i][j], DIST[i][k] + DIST[k][j])
    return DIST


def topological(N, LIST):  # トポロジカルソート:DAGに適用可
    # LIST:有向辺リスト
    from collections import deque

    incnt = [0] * N
    CHILD = [set() for _ in range(N)]
    for a, b in LIST:
        CHILD[a - 1].add(b - 1)
        incnt[b - 1] += 1

    TPLGSORT = []
    que = deque([i for i, num in enumerate(incnt) if num == 0])
    while que:
        q = que.popleft()
        for i in CHILD[q]:
            incnt[i] -= 1
            if incnt[i] == 0:
                que.append(i)
        TPLGSORT.append(q)
    return TPLGSORT


def prim(N, NEAR):  # プリム法:最小全域木
    from heapq import heappush, heappop, heapify

    flag = [0] * N
    flag[0] = 1
    que = [(c, j, 0) for j, c in NEAR[0]]
    heapify(que)

    ans = []
    while que:
        c_pq, q, p = heappop(que)
        if flag[q]:
            continue
        flag[q] = 1
        ans.append((p, q, c_pq))
        for r, c_qr in NEAR[q]:
            if 1 - flag[r]:
                heappush(que, (c_qr, r, q))
    return ans


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

    def same(self, x, y):  # 同じグループか否か
        return self.find(x) == self.find(y)

    def roots_cnt(self):  # 根の数
        return sum(x < 0 for x in self.parents)

    def roots(self):  # 根のリスト
        return [i for i, x in enumerate(self.parents) if x < 0]

    def size(self, x):  # 特定のグループのサイズ
        return - self.parents[self.find(x)]

    def all_sizes(self):  # 全てのグループのサイズ
        return {i: -x for i, x in enumerate(self.parents) if x < 0}

    def member(self, x):  # 特定のグループの要素
        root = self.find(x)
        return [i for i in range(self.N) if self.find(i) == root]

    def all_members(self):  # 全てのグループごとの要素
        group = {i: set() for i, x in enumerate(self.parents) if x < 0}
        for i in range(self.N):
            group[self.find(i)].add(i)
        return group
