from heapq import heappop, heappush
from collections import defaultdict


class Segtree():
    def segfunc(self, x, y):
        return min(x, y)

    def __init__(self, LIST, ELE):
        self.n, self.ide_ele = len(LIST), ELE
        self.num = 1 << (self.n - 1).bit_length()
        self.tree = [ELE] * 2 * self.num
        for i in range(self.n):
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


def main():
    rate = [[] for _ in range(M)]
    flag = [defaultdict(int) for _ in range(M)]
    now = []
    for i, (ai, bi) in enumerate(AB):
        now.append(bi-1)
        flag[bi-1][i] = 1
        heappush(rate[bi-1], (-ai, i))

    seg = Segtree([MAX]*M, MAX)
    for i, ri in enumerate(rate):
        if ri:
            seg.update(i, -ri[0][0])

    ans = []
    for ci, di in CD:
        ci, di = ci-1, di-1
        c_bfo, c_rate = now[ci], AB[ci][0]
        now[ci] = di

        flag[c_bfo][ci] = 0
        rate_cbfo = rate[c_bfo]
        while rate_cbfo and flag[c_bfo][rate_cbfo[0][1]] == 0:
            heappop(rate_cbfo)
        seg.update(c_bfo, (-rate_cbfo[0][0] if rate_cbfo else MAX))

        flag[di][ci] = 1
        heappush(rate[di], (-c_rate, ci))
        seg.update(di, -rate[di][0][0])
        ans.append(seg.query(0, M))
    return print(*ans, sep='\n')


if __name__ == '__main__':
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    CD = [list(map(int, input().split())) for _ in range(Q)]
    M, MAX = 2*10**5, 10**10

    main()
