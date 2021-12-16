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

class compression():
    
    def __init__(self, *ite):
        ite = sum(map(list, ite), [])
        self.lst = sorted(set(ite))
        self.dic = {k:i for i, k in enumerate(self.lst)}
    
    def zip(self, x):
        return self.dic[x]

def main():
    from collections import Counter

    ans = 0
    cnt = Counter((A[i], -B[i]) for i in range(N))
    cmp = compression(B)
    fen = Fenwicktree(N)
    for (_, bi), ci in sorted(cnt.items()):
        bi = cmp.zip(-bi)
        fen.update(bi ,ci)
        ans += ci * fen.query(bi, N)
    return print(ans)


if "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    main()