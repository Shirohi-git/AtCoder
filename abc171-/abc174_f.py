class Fenwicktree():  # Fenwicktree # 0-indexed
    def __init__(self, n):
        self.n = n
        self.tree = [0] * n

    def accsum(self, i):  # 区間和[0, i]
        i, res = i + 1, 0
        while i > 0:
            res += self.tree[i - 1]
            i -= i & -i
        return res

    def update(self, i, x):  # lst[i] += x
        i += 1
        while i <= self.n:
            self.tree[i - 1] += x
            i += i & -i

    def query(self, i, j):  # 区間和[i ,j)
        return self.accsum(j - 1) - self.accsum(i - 1)


n, q = map(int, input().split())
c = list(map(int, input().split()))
lr = [list(map(int, input().split())) for i in range(q)]
for i, (l, r) in enumerate(lr):
    lr[i] = (r << 40) + (l << 20) + i

fn = Fenwicktree(n)
cnt, place = 0, [-1] * n
ans = [0] * q
for num in sorted(lr):
    r, num = divmod(num, 1 << 40)
    l, i = divmod(num, 1 << 20)
    for j in range(cnt, r):
        color = c[j] - 1
        if place[color] >= 0:
            fn.update(place[color], -1)
        fn.update(j, 1)
        place[color] = j
    cnt = r
    ans[i] = fn.query(l - 1, r)
print(*ans, sep='\n')
