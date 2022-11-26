from collections import defaultdict


class Unionfind:
    def __init__(self, n0):
        self.len = n0
        self.parents = defaultdict(lambda: -1)
        self.boxname = defaultdict(int)
        self.boxball = defaultdict(int)
        for i in range(1, n0+1):
            self.boxball[i] = i
            self.boxname[i] = i

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
        box = self.boxname[x]
        self.boxname[y] = box

        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.boxball[box] = x


def main():
    uf = Unionfind(N)
    for q in OP:
        if q[0] == 1:
            if uf.boxball[q[2]] == None:
                continue
            elif uf.boxball[q[1]] == None:
                uf.boxball[q[1]] = uf.boxball[q[2]]
                uf.boxname[uf.boxball[q[2]]] = q[1]
            else:
                uf.unite(uf.boxball[q[1]], uf.boxball[q[2]])
            uf.boxball[q[2]] = None
        elif q[0] == 2:
            uf.len += 1
            if uf.boxball[q[1]] == None:
                uf.boxball[q[1]] = uf.len
                uf.boxname[uf.len] = q[1]
            else:
                uf.unite(uf.boxball[q[1]], uf.len)
        elif q[0] == 3:
            print(uf.boxname[uf.find(q[1])])
    return


if __name__ == '__main__':
    N, Q = map(int, input().split())
    OP = [list(map(int, input().split())) for _ in range(Q)]

    main()
