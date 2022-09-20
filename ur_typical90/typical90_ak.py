class Segtree():

    def __init__(self, size, ELE):
        n, self.ide_ele = size, ELE
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ELE] * 2 * self.num

    def query(self, l, r):
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if r & 1:
                res = max(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

    def getval(self, k):
        return self.tree[self.num + k]

    def point_update(self, k, x):
        self.tree[self.num + k] = x

    def all_update(self):
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])


def main():
    seg = Segtree(W+1, MININF)
    seg.point_update(0, 0)
    for l, r, v in LRV:
        seg.all_update()
        for j in range(W, l-1, -1):
            tmp = seg.query(max(0, j-r), j-l+1)
            if tmp + v > max(seg.getval(j), 0):
                seg.point_update(j, tmp + v)
    ans = seg.getval(W)
    return print(ans if ans > 0 else -1)


if __name__ == '__main__':
    W, N = map(int, input().split())
    LRV = [map(int, input().split()) for _ in range(N)]
    MININF = -(10 ** 9 + 1)

    main()
