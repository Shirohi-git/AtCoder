class Unionfind():
    def __init__(self, N):
        self.N = N
        self.parents = [-1] * N

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
        self.parents[y] = x

    def roots_cnt(self):
        return sum(x < 0 for x in self.parents)


n = int(input())
f = list(map(int, input().split()))
MOD9 = 998244353

uf = Unionfind(n)
for i, fi in enumerate(f):
    uf.union(i, fi - 1)
ans = 2 ** uf.roots_cnt() - 1
print(ans % MOD9)
