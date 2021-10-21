class Unionfind():
    def __init__(self, n0):
        self.n = n0
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

    def all_sizes(self):
        return {i: -x for i, x in enumerate(self.parents) if x < 0}


def main():
    uf = Unionfind(max(A)+1)
    for i in range(N):
        uf.unite(A[i], A[N-1-i])
    cnt = uf.all_sizes()

    ans = 0
    for ci in cnt.values():
        ans += ci - 1
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
