class Segtree:
    # 区間にしたい操作 ex) max,min,gcd,lcm,sum,product
    def segfunc(self, x, y):
        return max(x, y)

    # LIST: 配列の初期値, ELE: 単位元
    def __init__(self, LIST, ELE):
        self.n, self.ide_ele = len(LIST), ELE
        n = self.n
        self.num = 1 << (n - 1).bit_length()
        tree = self.tree = [ELE] * 2 * self.num
        for i in range(n):
            tree[self.num + i] = LIST[i]
        for i in range(self.num - 1, 0, -1):
            tree[i] = self.segfunc(tree[2 * i], tree[2 * i + 1])

    # k番目の値をxに更新
    def update(self, k, x):
        tree = self.tree
        k += self.num
        tree[k] = x
        while k > 1:
            tree[k >> 1] = self.segfunc(tree[k], tree[k ^ 1])
            k >>= 1

    # [l, r)のsegfuncしたものを得る
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

    # k番目の値を返す
    def getval(self, k):
        return self.tree[self.num + k]

    # print用 各indexの値がいくつになっているか
    def __str__(self):
        res = [str(self.tree[self.num + i]) for i in range(self.n)]
        return ' '.join(res)


def main():
    seg = Segtree([*range(N)][::-1], 0)
    ans = []
    for ai in A:
        seg.update(ai-1, seg.getval(ai-1) + N)
        ans.append(N - seg.query(0, N) % N)
    return print(*ans, sep='\n')


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    main()
