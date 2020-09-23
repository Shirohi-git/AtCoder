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

    def size(self, x):  # グループのサイズ
        return -self.parents[self.find(x)]


n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
xysort = [None] * n
for x, y in xy:
    xysort[x - 1] = y - 1

# 解説AC O(n)
uf = Unionfind(n)
cnt, yflag = 0, [0] * n
for x, y in enumerate(xysort[:-1]):
    yflag[y] = 1
    cnt += yflag[n - x - 1] + (y > n - x - 1)
    if cnt < x + 1:
        uf.union(x, x + 1)

for x, y in xy:
    print(uf.size(x - 1))
