class Segtree():

    def segfunc(self, x, y):
        if (x[0] > y[0]) or (x[0] == y[0] and x[2] > y[2]):
            x, y = y, x
        return x

    def __init__(self, LIST, ELE):
        self.ide_ele = ELE
        self.num = 1 << n.bit_length()
        self.tree = [ELE] * 2 * self.num
        for i in range(n + 1):
            self.tree[self.num + i] = LIST[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            p, q = min(k, k ^ 1), max(k, k ^ 1)
            self.tree[k >> 1] = self.segfunc(self.tree[p], self.tree[q])
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


n, m = map(int, input().split())
s = input()

num = 1 << n.bit_length()
dp = Segtree([(10 ** 6, -1, i) for i in range(n + 1)], (10 ** 6, -1, -1))
dp.update(0, (0, -1, 0))

for i, si in enumerate(s[1:], 1):
    if si == '0':
        cnt, _, bfo = dp.query(max(i - m, 0), i)
        dp.update(i, (cnt + 1, bfo, i))

now, (_, bfo, _) = n, dp.tree[num + n]
ans = [now - bfo]
while bfo != -1:
    now, (_, bfo, _) = bfo, dp.tree[num + bfo]
    ans.append(now - bfo)

print(*(ans[::-1][1:] if now == 0 else [-1]))
