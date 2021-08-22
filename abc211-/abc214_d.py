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

    def size(self, x):
        return - self.parents[self.find(x)]


def main():
    ans = 0
    uf = Unionfind(N)
    for u, v, w in sorted(UVW, key=lambda x: x[2]):
        ans += w * uf.size(u-1) * uf.size(v-1)
        uf.unite(u-1, v-1)

    return print(ans)


if __name__ == '__main__':
    N = int(input())
    UVW = [list(map(int, input().split())) for _ in range(N-1)]

    main()
