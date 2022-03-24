class Compression():
    def __init__(self, *ite):
        ite = sum(map(list, ite), [])
        self.lst = sorted(set(ite))
        self.dic = {k: i for i, k in enumerate(self.lst)}

    def zip(self, key):
        return self.dic[key]


class Segtree():
    def segfunc(self, x, y):
        (xv, xc), (yv, yc) = x, y
        return (xv + yv, xc + yc)

    def __init__(self, LIST, ELE):
        self.n, self.ide_ele = len(LIST), ELE
        n = self.n
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ELE] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = LIST[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = self.segfunc(self.tree[k], x)
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


def main():
    cmp = Compression([0] + [y for _, _, y in TXY])
    a_seg = Segtree([(0, N)] + [ELE] * Q, ELE)
    b_seg = Segtree([(0, M)] + [ELE] * Q, ELE)

    a, b = [0] * N, [0] * M
    ans = 0
    for t, x, y in TXY:
        if t == 1:
            lst, up_seg, sum_seg = a, a_seg, b_seg
        if t == 2:
            lst, up_seg, sum_seg = b, b_seg, a_seg

        abx_id = cmp.zip(lst[x-1])
        ans -= lst[x-1] * sum_seg.query(0, abx_id)[1]
        ans -= sum_seg.query(abx_id, Q+1)[0]
        up_seg.update(abx_id, (-lst[x-1], -1))

        y_id = cmp.zip(y)
        up_seg.update(y_id, (y, 1))
        ans += y * sum_seg.query(0, y_id)[1]
        ans += sum_seg.query(y_id, Q+1)[0]

        lst[x-1] = y
        print(ans)
    return


if __name__ == '__main__':
    N, M, Q = map(int, input().split())
    TXY = [list(map(int, input().split())) for _ in range(Q)]
    ELE = (0, 0)

    main()
