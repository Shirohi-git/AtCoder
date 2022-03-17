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
    ans = [0]
    bit = Fenwicktree(N)
    for ai in A:
        bit.update(ai, 1)
        ans[-1] += bit.query(ai+1, N)

    for ai in A[:-1]:
        ans.append(ans[-1])
        ans[-1] += bit.query(ai+1, N)
        ans[-1] -= bit.query(0, ai)
    return print(*ans, sep='\n')


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
