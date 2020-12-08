from itertools import accumulate


def diff(x, y, z):
    return abs((a[y] - a[x]) - (a[z] - a[y]))


def cal(x, y, z):
    lst = a[x] - a[0], a[y] - a[x], a[z] - a[y], a[n] - a[z]
    return max(lst) - min(lst)


n = int(input())
a = [0] + list(accumulate(map(int, input().split())))

l, r, ans = 1, 3, cal(1, 2, 3)
for cen in range(2, n - 1):
    l, r = min(l, cen - 1), max(r, cen + 1)
    while diff(0, l, cen) >= diff(0, l + 1, cen):
        if l == cen - 1:
            break
        l += 1
    while diff(cen, r, n) >= diff(cen, r + 1, n):
        if r == n - 1:
            break
        r += 1
    ans = min(ans, cal(l, cen, r))
print(ans)
