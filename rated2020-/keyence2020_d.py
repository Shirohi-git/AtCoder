class Fenwicktree():
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
        if i > self.n:
            raise IndexError
        j = min(self.n, j)
        return self.accsum(j - 1) - self.accsum(i - 1)


def inversion_number(n0, lst0):
    res = 0
    bit = Fenwicktree(n0)
    for li in lst0:
        bit.update(li, 1)
        res += bit.query(li+1, n0)
    return res


def check(e, o):
    card, ids = [], []
    if not 0 <= len(e)-len(o) <= 1:
        return -1
    e.sort(), o.sort()
    for i in range(N):
        ci = (o if i % 2 else e)[i // 2]
        card.append(ci[0]), ids.append(ci[1])
    if card != sorted(card):
        return -1
    res = inversion_number(N, ids)
    return res


def main():
    ans = N**2
    for bit in range(1<<N):
        evn, odd = [], []
        for i in range(N):
            on = bit >> i & 1
            num = (B[i] if on else A[i])
            lst = (odd if on ^ (i % 2) else evn)
            lst.append((num, i))
        cost = check(evn, odd)
        if cost > -1:
            ans = min(cost, ans)
    return print(ans if ans < N**2 else -1)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    main()