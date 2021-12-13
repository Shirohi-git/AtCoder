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
        self.parents[y] += self.parents[x]
        self.parents[x] = y


def main():
    a = [-1] * N
    nxt = Unionfind(N)
    for t, x in TX:
        if t == 1:
            h = x % N
            while a[h] > -1:
                nxt.unite(h, (h+1) % N)
                h = nxt.find(h)
            a[h] = x
        if t == 2:
            print(a[x % N])
    return


if __name__ == '__main__':
    Q = int(input())
    TX = [list(map(int, input().split())) for _ in range(Q)]
    N = 1 << 20

    main()
