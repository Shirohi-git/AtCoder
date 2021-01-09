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

    def members(self):
        group = {i: set() for i, x in enumerate(self.parents) if x < 0}
        for i in range(self.N):
            group[self.find(i)].add(i)
        return group


n = int(input())
ab = [map(int, input().split()) for _ in range(n)]

uf = Unionfind(400000)
cnt = [0 for _ in range(400000)]
for a, b in ab:
    uf.union(a - 1, b - 1)
    cnt[a - 1] += 1
    cnt[b - 1] += 1

ans = 0
for v in uf.members().values():
    ans += min(len(v), sum(cnt[vi] for vi in v) // 2)
print(ans)
