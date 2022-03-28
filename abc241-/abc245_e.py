class Compression():
    def __init__(self, *ite):
        ite = sum(map(list, ite), [])
        self.lst = sorted(set(ite))
        self.dic = {k: i for i, k in enumerate(self.lst)}

    def zip(self, key):
        return self.dic[key]


class Segtree():
    def segfunc(self, x, y):
        return min(x, y)

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
        self.tree[k] = x
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

    def getval(self, k):
        return self.tree[self.num + k]


def main():
    cmp = Compression(B+D)
    w_seg = Segtree([(INF, 0)] * (N+M), (INF, 0))
    ab = list(zip(A, B, [0] * N))
    cd = list(zip(C, D, [1] * M))
    for _, wi, box in sorted(ab + cd)[::-1]:
        wi = cmp.zip(wi)
        if box:
            cnt = w_seg.getval(wi)[1]
            w_seg.update(wi, (wi, cnt+1))
        else:
            idx, cnt = w_seg.query(wi, N+M)
            if idx == INF:
                return print("No")
            w_seg.update(idx, (idx if cnt > 1 else INF, cnt-1))
    return print("Yes")


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))
    INF = 10**6

    main()
