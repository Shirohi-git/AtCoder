import sys
input = sys.stdin.readline


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

    def same(self, x, y):  # 同じグループか否か
        return self.find(x) == self.find(y)


# 解説AC
n, m, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
cd = [list(map(int, input().split())) for _ in range(k)]

uf = Unionfind(n)
frnd = [0] * n
for a, b in ab:
    uf.union(a - 1, b - 1)
    frnd[a - 1] += 1
    frnd[b - 1] += 1

brck = [0] * n
for c, d in cd:
    if uf.same(c - 1, d - 1):
        brck[c - 1] += 1
        brck[d - 1] += 1

ans = []
for i in range(n):
    ans.append(uf.size(i) - frnd[i] - brck[i] - 1)
print(*ans)
