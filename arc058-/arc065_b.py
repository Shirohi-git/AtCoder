from collections import Counter


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
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x


n, k, l = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(k)]
train = [list(map(int, input().split())) for _ in range(l)]

r_uf, t_uf = Unionfind(n), Unionfind(n)
for x, y in road:
    r_uf.union(x-1, y-1)
for x, y in train:
    t_uf.union(x-1, y-1)
lst = [r_uf.find(i) * n + t_uf.find(i) for i in range(n)]
cnt = Counter(lst)
ans = [cnt[lst[i]] for i in range(n)]
print(*ans)
