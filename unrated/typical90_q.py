class Fenwicktree():

    def __init__(self, n):
        self.n = n
        self.tree = [0] * n

    def accsum(self, i):
        i, res = i + 1, 0
        while i > 0:
            res += self.tree[i - 1]
            i -= i & -i
        return res

    def update(self, i, x):
        i += 1
        while i <= self.n:
            self.tree[i - 1] += x
            i += i & -i

    def query(self, i, j):
        return self.accsum(j - 1) - self.accsum(i - 1)


def main():
    n, m = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(m)]
    lr = sorted((l-1, -r+1) for l, r in lr)

    bit = Fenwicktree(n)
    ans = 0
    for l, r in lr:
        bit.update(-r, 1)
        ans += bit.query(l+1, -r)
    print(ans)


if __name__ == '__main__':
    main()
