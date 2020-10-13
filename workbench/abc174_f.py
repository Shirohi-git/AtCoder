class Fenwicktree():  # Fenwicktree # 1-indexed
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def accsum(self, i):  # 区間和[0, i]
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def update(self, i, x):  # lst[i] +=x
        while i <= self.n:
            self.tree[i] += x
            i += i & -i

    def query(self, i, j):  # 区間和[i ,j)
        return self.accsum(j - 1) - self.accsum(i - 1)


n, q = map(int, input().split())
c = list(map(int, input().split()))
lr = [list(map(int, input().split())) for i in range(q)]
for i, (l, r) in enumerate(lr):
    tmp = (r << 40) + (l << 20) + i
    lr[i] = tmp

fn = Fenwicktree(n)
cnt, place = 1, [-1] * n
ans = [0] * q
for num in sorted(lr):
    r, num = divmod(num, 1 << 40)
    l, i = divmod(num, 1 << 20)
    for j in range(cnt, r + 1):
        color = c[j - 1] - 1
        if place[color] > 0:
            fn.update(place[color], -1)
        fn.update(j, 1)
        place[color] = j
    cnt = r + 1
    ans[i] = fn.query(l, r + 1)
print(*ans, sep='\n')
