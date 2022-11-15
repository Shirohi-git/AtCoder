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

    def same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    uf = Unionfind(H*W)
    near = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    x, y = -1, -1

    for i, ci in enumerate(C):
        for j, cij in enumerate(ci):
            if cij == 'S':
                x, y = i, j
            if cij != '.':
                continue
            for di, dj in near:
                if 0 <= i+di < H and 0 <= j+dj < W:
                    if C[i+di][j+dj] == '.':
                        uf.unite(W*i+j, W*(i+di)+j+dj)
    res = False
    for i, (dx, dy) in enumerate(near):
        if not (0 <= x+dx < H and 0 <= y+dy < W):
            continue
        for dp, dq in near[:i]:
            if 0 <= x+dp < H and 0 <= y+dq < W:
                a, b = W*(x+dx)+(y+dy), W*(x+dp)+(y+dq)
                res |= uf.same(a, b)
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]

    main()
