class Unionfind():
    def __init__(self, n0):
        self.n = n0
        self.parents = [-1] * n0

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)


def kruskal():
    edge = []
    for i, ni in enumerate(NEAR):
        edge += [(c, i, j) for j, c in ni if i < j]
    edge = sorted(edge)

    res = 0
    for w, i, j in edge:
        if not UF.same(i, j):
            res += w
            UF.unite(i, j)
    return res


def make_edge(p, q):
    (px, py, id1), (qx, qy, id2) = p, q
    cx = min(abs(px - qx), abs(py - qy))
    NEAR[id1].add((id2, cx)), NEAR[id2].add((id1, cx))
    return


def main():
    x_sort = sorted((xi, yi, i) for i, (xi, yi) in enumerate(XY))
    y_sort = sorted((yi, xi, i) for i, (xi, yi) in enumerate(XY))
    for i in range(1, N):
        make_edge(x_sort[i-1], x_sort[i])
        make_edge(y_sort[i-1], y_sort[i])
    ans = kruskal()
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    NEAR = [set() for _ in range(N)]
    UF = Unionfind(N)
    main()
