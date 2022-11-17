from collections import defaultdict


class Unionfind:
    def __init__(self):
        self.parents = defaultdict(lambda: -1)

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

    def member(self, x):
        root = self.find(x)
        return [i for i in self.parents if self.find(i) == root]


def main():
    uf = Unionfind()
    for ai, bi in AB:
        uf.unite(ai, bi)
    ans = max(uf.member(1))
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]

    main()
