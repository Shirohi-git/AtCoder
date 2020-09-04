def nearlist(N, LIST):  # 隣接リスト
    NEAR = [set() for _ in range(N)]
    for a, b in LIST:
        NEAR[a - 1].add(b - 1)
        NEAR[b - 1].add(a - 1)
    return NEAR


def bfs(NEAR, S, N):  # 幅優先探索  # キュー
    # 隣接リスト,始点,数
    from collections import deque

    dist = [-1 for _ in range(N)]  # 前処理
    path = [-1 for _ in range(N)]
    dist[S], path[S] = 0, 's'
    que, frag = deque([S]), set([S])

    while que:
        q = que.popleft()
        for i in NEAR[q]:  # 移動先の候補
            if i in frag:  # 処理済みか否か
                continue
            # 処理を行う
            que.append(i), frag.add(i)
    return


def dfs(NEAR, S, N):  # 深優先探索  # スタック
    # 隣接リスト,始点,数

    dist = [-1 for _ in range(N)]  # 前処理
    path = [-1 for _ in range(N)]
    dist[S], path[S] = 0, 's'
    stack, frag = [S], set([S])

    while stack:
        q = stack.pop()
        for i in NEAR[q]:  # 移動先の候補
            if i in frag:  # 処理済みか否か
                continue
            # 処理を行う
            stack.append(i), frag.add(i)
    return


class Recursive_dfs():  # 深優先探索(再帰)
    import sys
    sys.setrecursionlimit(10 ** 7)

    def __init__(self, NEAR, S, N):
        # 隣接リスト,始点,数
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


def warshallfloyd(N, LIST):  # ワーシャルフロイド法:全頂点対最短経路 O(n**3)
    # LIST:隣接行列
    from copy import deepcopy
    DIST = LIST.deepcopy()
    for k in range(N):
        for i in range(N):
            for j in range(N):
                DIST[i][j] = min(DIST[i][j], DIST[i][k] + DIST[k][j])
    return DIST


def topological(N, LIST):  # トポロジカルソート:DAGに適用可
    # 頂点数, 辺リスト
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

    def groups(self):  # 全てのグループごとの要素
        group = {i: set() for i, x in enumerate(self.parents) if x < 0}
        for i in range(self.N):
            group[self.find(i)].add(i)
        return group

    def size(self, x):  # グループのサイズ
        return -self.parents[self.find(x)]

    def same(self, x, y):  # 同じグループか否か
        return self.find(x) == self.find(y)

    def members(self, x):  # 特定のグループの要素
        root = self.find(x)
        return [i for i in range(self.N) if self.find(i) == root]

    def roots(self):  # 根のリスト
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_cnt(self):  # グループの数
        return sum(x < 0 for x in self.parents)
