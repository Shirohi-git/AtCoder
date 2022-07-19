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
    uf = Unionfind(N + 2)
    for i, (x1, y1, r1) in enumerate(XYR):
        for j, (x2, y2, r2) in enumerate(XYR[i+1:], i+1):
            if (r1-r2)**2 <= (x1-x2)**2 + (y1-y2)**2 <= (r1+r2)**2:
                uf.unite(i, j)
    return print('Yes' if uf.same(0, N+1) else 'No')


if __name__ == '__main__':
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    XYR = [list(map(int, input().split())) for _ in range(N)]
    XYR = [[sx, sy, 0]] + XYR + [[tx, ty, 0]]

    main()
