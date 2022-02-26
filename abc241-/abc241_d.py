class Compression():
    def __init__(self, *ite):
        ite = sum(map(list, ite), [])
        self.lst = sorted(set(ite))
        self.dic = {k: i for i, k in enumerate(self.lst)}

    def zip(self, key):
        return self.dic[key]

    def unzip(self, idx):
        ans = self.lst[idx]
        return -1 if ans in [0, MAX] else self.lst[idx]


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
    def binary(s, cnt, ok, op):
        if a.query(s, s+1) >= cnt:
            return s
        ng = s
        def is_OK(m):
            if op == 2:
                res = (a.query(m, s+1) >= cnt)
            elif op == 3:
                res = (a.query(s, m+1) >= cnt)
            return res

        while abs(ng - ok) > 1:
            mid = (ok + ng) // 2
            if is_OK(mid):
                ok = mid
            else:
                ng = mid
        return ok

    query = [(qi + [0])[:3] for qi in Query]
    cmp = Compression([qi[1] for qi in query] + [0] + [MAX])
    a = Fenwicktree(cmp.zip(MAX)+1)
    a.update(0, 10), a.update(cmp.zip(MAX), 10)
    for op, x, k in query:
        if op == 1:
            a.update(cmp.zip(x), 1)
        elif op == 2:
            idx = binary(cmp.zip(x), k, cmp.zip(0), op)
            print(cmp.unzip(idx))
        elif op == 3:
            idx = binary(cmp.zip(x), k, cmp.zip(MAX), op)
            print(cmp.unzip(idx))
    return


if __name__ == '__main__':
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]
    MAX = 10**19
    main()
