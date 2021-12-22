class Unionfind():
    def __init__(self, n0):
        self.n = n0
        self.parents = [-1] * n0
        self.edgecnt = [0] * n0

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
        self.edgecnt[x] += 1

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.edgecnt[x] += self.edgecnt[y]
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def is_no_cycle(self):
        res = 1
        for x, c in zip(self.parents, self.edgecnt):
            if x < 0:
                res &= (-x > c)
        return res


def main():
    uf = Unionfind(N)
    cnt = [0] * N

    for ai, bi in AB:
        uf.unite(ai-1, bi-1)
        cnt[ai-1] += 1
        cnt[bi-1] += 1

    res = all(ci < 3 for ci in cnt)
    res &= uf.is_no_cycle()
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    main()
