from collections import defaultdict


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


def inversion_number(n0, lst):
    res = 0
    bit = Fenwicktree(n0)
    for li in lst:
        bit.update(li, 1)
        res += bit.query(li+1, n0)
    return res


def main():
    a = [A[i] + i for i in range(N)]
    b = [B[i] + i for i in range(N)]
    b_idx = defaultdict(list)
    for i in range(N)[::-1]:
        b_idx[b[i]].append(i)

    ans = 0
    res = []
    for ai in a:
        if not b_idx[ai]:
            return print(-1)
        res.append(b_idx[ai].pop())
    ans = inversion_number(len(res), res)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    main()
