class Unionfind:
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


def main():
    uf = Unionfind(N)
    for a, b in AB:
        uf.unite(a-1, b-1)
    ans = max(0, M-N+uf.len)
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    main()