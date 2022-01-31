from itertools import accumulate


class Compression():

    def __init__(self, *ite):
        ite = sum(map(list, ite), [])
        self.lst = sorted(set(ite))
        self.dic = {k: i for i, k in enumerate(self.lst)}

    def zip(self, key):
        return self.dic[key]
    
    def unzip(self, idx):
        return self.lst[idx]


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


def main():
    a = [ai - K for ai in A]
    
    ans = 0
    acc = list(accumulate([0] + a))
    cnt = Fenwicktree(N+1)
    cmp = Compression(acc)
    for ai in acc:
        idx = cmp.zip(ai)
        ans += cnt.accsum(idx)
        cnt.update(idx, 1)
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(int(input()) for _ in range(N))

    main()