class Unionfind():
    def __init__(self, n0):
        self.n = n0
        self.parents = [-1] * n0
        self.edge_cnt = [0] * n0

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
        self.edge_cnt[x] += self.edge_cnt[y]
        self.edge_cnt[y] = -1
        return

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def is_EeqV(self, x):
        x = self.find(x)
        return self.edge_cnt[x] == - self.parents[x]

    def add_edge(self, x):
        self.edge_cnt[self.find(x)] += 1
        return


def main():
    uf = Unionfind(N)
    for u, v in UV:
        uf.unite(u-1, v-1)
        uf.add_edge(u-1)
    ans = pow(2, len(uf.roots()), MOD9)
    ans *= all(uf.is_EeqV(x) for x in uf.roots())
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    UV = [map(int, input().split()) for _ in range(M)]
    MOD9 = 998244353

    main()
