class Compression():
    def __init__(self, *ite):
        ite = sum(map(list, ite), [])
        self.lst = sorted(set(ite))
        self.dic = {k: i for i, k in enumerate(self.lst)}
        self.len = len(self.lst)

    def zip(self, key):
        return self.dic[key]


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
        j = min(self.n, j)
        return self.accsum(j - 1) - self.accsum(i - 1)


def main():
    c_num = {ci: [] for ci in C}
    for ci, xi in zip(C, X):
        c_num[ci].append(xi)
    c_cmp = {k: Compression(v) for k, v in c_num.items()}

    ans = 0
    bit = Fenwicktree(N+1)
    c_bit = {k: Fenwicktree(v.len) for k, v in c_cmp.items()}
    for ci, xi in zip(C, X):
        ci_xi = c_cmp[ci].zip(xi)
        bit.update(xi, 1), c_bit[ci].update(ci_xi, 1)
        ans += bit.query(xi+1, N+1)
        ans -= c_bit[ci].query(ci_xi+1, N+1)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    C = list(map(int, input().split()))
    X = list(map(int, input().split()))

    main()
