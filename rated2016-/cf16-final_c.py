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


n, m = map(int, input().split())
lang = [list(map(int, input().split()))[1:] for _ in range(n)]

uf = Unionfind(n + m)
for i, li in enumerate(lang):
    for lij in li:
        uf.union(i, lij - 1 + n)
torf = all(uf.find(0) == uf.find(i) for i in range(1, n))
print('YES' if torf else 'NO')
