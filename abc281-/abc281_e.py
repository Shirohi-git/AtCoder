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


class Compression:
    def __init__(self, *ite):
        ite = sum(map(list, ite), [])
        self.lst = sorted(set(ite))
        self.dic = {k: i for i, k in enumerate(self.lst)}
        self.len = len(self.lst)

    def zip(self, key):
        return self.dic[key]


def main():
    def find_K(ok=N-1, ng=0):
        def is_OK(num):
            return bit_cnt.accsum(num) >= K

        while abs(ng - ok) > 1:
            mid = (ok + ng) // 2
            if is_OK(mid):
                ok = mid
            else:
                ng = mid
        return ok

    cmp = Compression([(ai, i) for i, ai in enumerate(A)])
    a = [cmp.zip((ai, i)) for i, ai in enumerate(A)]
    bit = Fenwicktree(N)
    bit_cnt = Fenwicktree(N)
    for id, ai in zip(a[:M], A[:M]):
        bit.update(id, ai)
        bit_cnt.update(id, 1)

    ans = [bit.accsum(find_K())]
    for bfo_k, bfo_v, now_k, now_v in zip(a, A, a[M:], A[M:]):
        bit_cnt.update(bfo_k, -1), bit_cnt.update(now_k, 1)
        bit.update(bfo_k, -bfo_v), bit.update(now_k, now_v)
        ans.append(bit.accsum(find_K()))
    return print(*ans)


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))

    main()
