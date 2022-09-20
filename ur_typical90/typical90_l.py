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

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)


h, w = map(int, input().split())
q = int(input())
query = [list(map(int, input().split())) for _ in range(q)]

grid = [0] * (h*w)
uf = Unionfind(h*w)
for qi in query:
    qi = [qij-1 for qij in qi]
    idx1 = qi[1] * w + qi[2]
    if qi[0] == 0:
        grid[idx1] = 1
        if (qi[1] > 0 and grid[idx1 - w]):
            uf.unite(idx1, idx1 - w)
        if (qi[1] + 1 < h and grid[idx1 + w]):
            uf.unite(idx1, idx1 + w)
        if (qi[2] > 0 and grid[idx1 - 1]):
            uf.unite(idx1, idx1 - 1)
        if (qi[2] + 1 < w and grid[idx1 + 1]):
            uf.unite(idx1, idx1 + 1)
    elif qi[0] == 1:
        idx2 = qi[3] * w + qi[4]
        res = uf.same(idx1, idx2) & grid[idx1] & grid[idx2]
        print('Yes' if res else 'No')
