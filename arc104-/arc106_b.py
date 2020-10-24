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

    def groups(self):  # 全てのグループごとの要素
        group = {i: set() for i, x in enumerate(self.parents) if x < 0}
        for i in range(self.N):
            group[self.find(i)].add(i)
        return group


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cd = [list(map(int, input().split())) for _ in range(m)]

uf = Unionfind(n)
for c, d in cd:
    uf.union(c - 1, d - 1)
grp = uf.groups()

ans = 1
for mem in grp.values():
    suma = sum(a[i] for i in mem)
    sumb = sum(b[i] for i in mem)
    ans *= (suma == sumb)
print('Yes' if ans else 'No')
