class Compression:
    def __init__(self, *ite):
        ite = sum(map(list, ite), [])
        self.lst = sorted(set(ite))[::-1]
        self.dic = {k: i for i, k in enumerate(self.lst)}
        self.len = len(self.lst)

    def zip(self, key):
        return self.dic[key]

    def unzip(self, idx):
        return self.lst[idx]


class Fenwicktree:
    def __init__(self, n, ini=None):
        self.n = n
        self.tree = [0] * n
        if ini:
            for i, ni in enumerate(ini):
                self.update(i, ni)

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
        if i >= self.n:
            raise IndexError
        j = min(self.n, j)
        return self.accsum(j - 1) - self.accsum(i - 1)

    def lower_bound(self, x):
        idx, cnt = 0, 0
        for i in range((self.n-1).bit_length()+1)[::-1]:
            k = idx + (1 << i)
            if k <= self.n and cnt+self.tree[k-1] < x:
                cnt += self.tree[k-1]
                idx += 1 << i
        return idx

    def __setitem__(self, key, val):
        return self.update(key, val - self.query(key, key+1))

    def __getitem__(self, key): return self.query(key, key+1)


def main():

    def sum_kth():
        idx = bit_cnt.lower_bound(K)
        cnt = bit_cnt.query(0, idx)
        res = bit.query(0, idx)
        res += cmp.unzip(idx) * (K-cnt)
        return res

    a = [0] * N
    cmp = Compression([y for x, y in XY]+[0])
    bit = Fenwicktree(cmp.len)
    bit_cnt = Fenwicktree(cmp.len)
    bit_cnt[cmp.zip(0)] = N

    for x, y in XY:
        zx, zy = cmp.zip(a[x-1]), cmp.zip(y)
        bit_cnt.update(zx, -1), bit_cnt.update(zy, 1)
        bit.update(zx, -a[x-1]), bit.update(zy, y)
        a[x-1] = y
        print(sum_kth())
    return


if __name__ == '__main__':
    N, K, Q = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(Q)]

    main()
