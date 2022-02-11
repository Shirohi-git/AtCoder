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
    def nearlist(n0):
        res = [[] for _ in range(n0)]
        for a, b in AB:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        return res

    near = nearlist(N)
    uf = Unionfind(N)

    ans = [0]
    for i in range(1, N)[::-1]:
        res = ans[-1] + 1
        for q in near[i]:
            if q > i:
                res -= (1 - uf.same(i, q))
                uf.unite(i, q)
        ans.append(res)
    return print(*ans[::-1], sep='\n')


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    main()
