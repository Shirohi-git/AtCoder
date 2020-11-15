from collections import Counter


class Unionfind():
    def __init__(self, N):
        self.N = N
        self.parents = [-1] * N
        self.count = [0] * N

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        for k, v in self.count[y].items():
            self.count[x][k] += v
        self.parents[y] = x

    def size(self, x, y):
        return self.count[self.find(x)][y]


n, q = map(int, input().split())
c = list(map(int, input().split()))
query = [list(map(int, input().split())) for _ in range(q)]

uf = Unionfind(n)
for i, ci in enumerate(c):
    uf.count[i] = Counter({ci: 1})
for num, x, y in query:
    if num == 1:
        uf.union(x - 1, y - 1)
    if num == 2:
        print(uf.size(x - 1, y))
