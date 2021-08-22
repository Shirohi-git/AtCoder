class Unionfind():
    def __init__(self, n0):
        self.n = n0
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

    def same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    uf = Unionfind(N)
    for t, u, v in TUV:
        if t == 1:
            print(int(uf.same(u, v)))
        if t == 0:
            uf.unite(u, v)
    return


if __name__ == '__main__':
    N, Q = map(int, input().split())
    TUV = [list(map(int, input().split())) for _ in range(Q)]

    main()
