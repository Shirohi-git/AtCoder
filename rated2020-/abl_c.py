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

    def group_cnt(self):  # グループの数
        return sum(x < 0 for x in self.parents)

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

uf = Unionfind(n)
for a, b in ab:
    uf.union(a - 1, b - 1)
print(uf.group_cnt() - 1)
