from itertools import accumulate

n, m = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(m)]

num = [0] * (n + 1)
for l, r in lr:
    num[l - 1] += 1
    num[r] -= 1
num = list(accumulate(num))
print(num.count(m))
