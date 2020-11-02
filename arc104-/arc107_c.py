from itertools import combinations


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

    def sizes(self):
        return [-x for i, x in enumerate(self.parents) if x < 0]


n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
at = [list(a_j) for a_j in zip(*a)]
MOD = 998244353

row = Unionfind(n)
for x, y in combinations(range(n), 2):
    if all(axi + ayi <= k for axi, ayi in zip(a[x], a[y])):
        row.union(x, y)

col = Unionfind(n)
for x, y in combinations(range(n), 2):
    if all(aix + aiy <= k for aix, aiy in zip(at[x], at[y])):
        col.union(x, y)

fra = [0, 1]
for i in range(2, n + 1):
    fra.append(i * fra[-1] % MOD)

ans = 1
for s in (row.sizes() + col.sizes()):
    ans = ans * fra[s] % MOD
print(ans)
