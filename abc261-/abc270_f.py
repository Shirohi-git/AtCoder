class Unionfind():
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


def main():
    def kruskal(p):
        k_uf = Unionfind(N+2)
        res = 0
        for w, i, j in edge:
            if j == N and p & 1:
                continue
            if j == N+1 and p & 2:
                continue
            if not k_uf.same(i, j):
                res += w
                k_uf.unite(i, j)
        if k_uf.len <= 3:
            return res
        return INF
    
    # port, airport = N, N+1
    brdg = [(z, a-1, b-1) for a, b, z in ABZ]
    port = [(X[i], i, N) for i in range(N)]
    airp = [(Y[i], i, N+1) for i in range(N)]
    edge = sorted(brdg + port + airp)

    ans = INF
    for ptn in range(4):
        res = kruskal(ptn)
        ans = min(ans, res)
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    ABZ = [list(map(int, input().split())) for _ in range(M)]
    INF = 10**15

    main()
