from itertools import accumulate


def max_acc(lst):
    acc = list(accumulate(v for _, v in lst))
    res = [(0, 0)]
    for (x, _), a in zip(lst, acc):
        res.append(max(res[-1], (a - x, x)))
    return res


n, c = map(int, input().split())
xv = [list(map(int, input().split())) for _ in range(n)]
cxv = [[c - x, v] for x, v in xv[::-1]]

ans = 0
for (v, x), (cv, cx) in zip(max_acc(xv), max_acc(cxv)[::-1]):
    ans = max(ans, v + cv - min(x, cx))
print(ans)
