class Segtree():
    def __init__(self, n):
        self.num = 1 << (n - 1).bit_length()
        self.tree = [0] * 2 * self.num
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = max(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = 0
        l, r = l + self.num, r + self.num
        while l < r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if r & 1:
                res = max(res, self.tree[r - 1])
            l, r = l >> 1, r >> 1
        return res


n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

# 解説AC
a_max = max(a) + 1
seg_dp = Segtree(a_max)
for ai in a:
    tmp = seg_dp.query(max(ai - k, 0), min(ai + k + 1, a_max))
    seg_dp.update(ai, tmp + 1)
print(max(seg_dp.tree))
