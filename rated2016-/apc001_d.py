class Unionfind():
    def __init__(self, n0):
        self.n = n0
        self.len = n0
        self.parents = [-1] * n0

    def find(self, x):
        stack = []
        while self.parents[x] >= 0:
            stack.append(x)
            x = self.parents[x]
        for i in stack:
            self.parents[i] = x
        return x

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.len -= 1

    def all_members(self):
        group = {i: set() for i, x in enumerate(self.parents) if x < 0}
        for i in range(self.n):
            group[self.find(i)].add(i)
        return group


def main():
    uf = Unionfind(N)
    for x, y in XY:
        uf.unite(x, y)

    ans = 0
    all_wei = []
    for mem in uf.all_members().values():
        wei = [A[i] for i in mem]
        ans += min(wei)
        wei.remove(min(wei))
        all_wei += wei

    if uf.len-2 > len(all_wei):
        return print("Impossible")

    ans += sum(sorted(all_wei)[:uf.len-2])
    if uf.len == 1:
        ans = 0
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]

    main()
