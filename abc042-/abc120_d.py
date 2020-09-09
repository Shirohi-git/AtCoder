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
        return - self.parents[self.find(x)]


n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

uf = Unionfind(n)
ans, cnt = [], n * (n - 1) // 2
for a, b in ab[::-1]:
    a, b = a - 1, b - 1
    ans.append(max(cnt, 0))
    if uf.find(a) != uf.find(b):
        cnt -= uf.size(a) * uf.size(b)
        uf.union(a, b)
print(*ans[::-1], sep='\n')
