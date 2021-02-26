def makenum(n):
    t, res = 1, 0
    for xi in x[::-1]:
        res += xi * t
        t *= n
    return res


def binary(r, l):
    while abs(r - l) > 1:
        mid = (l + r) // 2
        if makenum(mid) <= m:
            r = mid
        else:
            l = mid
    return max(r - d, 0)


x = list(map(int, list(input())))
m, d = int(input()), max(x)

print(int(x[0] <= m) if len(x) == 1 else binary(0, m + 1))
