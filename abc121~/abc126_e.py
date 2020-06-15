class Unionfind():  # Unionfind
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

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

    def roots(self):  # 根のリスト
        return [i for i, x in enumerate(self.parents) if x < 0]


n, m = map(int, input().split())
xyz = sorted([list(map(int, input().split())) for _ in range(m)])

uf = Unionfind(n)
for x, y, z in xyz:
    uf.union(x - 1, y - 1)
print(len(uf.roots()))
