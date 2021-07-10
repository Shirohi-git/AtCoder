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
    flag = Fenwicktree(N-1)
    diff = Fenwicktree(N-1)
    for t, x, y, v in TXYV:
        if t == 0 and flag.query(x-1, x) == 0:
            flag.update(x-1, 1)
            diff.update(x-1, (v if x % 2 else -v))
        if t == 1:
            rev = (y < x)
            if y < x:
                x, y = y, x
            if flag.query(x-1, y-1) < y - x:
                print("Ambiguous")
                continue
            acc = diff.query(x-1, y-1)
            if (1 - rev and y % 2) or (rev and 1 - x % 2):
                acc = -acc
            print(acc-v if (y-x) % 2 else acc+v)
    return


if __name__ == '__main__':
    N, Q = int(input()), int(input())
    TXYV = [list(map(int, input().split())) for _ in range(Q)]

    main()
