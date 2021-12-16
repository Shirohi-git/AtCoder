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
    block = [[H] for _ in range(W)]
    for x, y in XY:
        block[y-1].append(x-1)
    row = Fenwicktree(H)
    for i in range(min(block[0])):
        row.update(i, 1)

    ans, flag = 0, 0
    for i in range(W):
        min_blk = min(block[i])
        if min_blk == 0 or flag:
            min_blk, flag = 0, 1
        for j in block[i]:
            if j < H and row.query(j, j+1):
                row.update(j, -1)
        ans += min_blk + row.query(min_blk, H)
    print(ans)


if __name__ == '__main__':
    H, W, M = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(M)]

    main()
