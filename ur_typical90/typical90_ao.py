from math import gcd


def convex_hull(point_lst):

    def is_CW(ax, ay, bx, by, cx=0, cy=0):
        res = (bx-cx) * (ay-cy) - (by-cy) * (ax-cx)
        return res > 0

    def half_hull(lst):
        res = []
        for pi in lst:
            while len(res) > 1 and is_CW(*pi, *res[-2], *res[-1]):
                res.pop()
            res.append(pi)
        return res

    point_lst = sorted(point_lst)
    res1 = half_hull(point_lst)
    res2 = half_hull(point_lst[::-1])
    return res1 + res2[1:]


def main():
    lst = convex_hull(XY)
    s, bd = 0, 0
    for i in range(len(lst) - 1):
        (xi, yi), (xj, yj) = lst[i], lst[i+1]
        s += (xi-xj) * (yi+yj)
        bd += gcd(abs(xi-xj), abs(yi-yj))
    intr = int(abs(s) - bd + 2) // 2
    ans = bd + intr - N
    print(ans)


if __name__ == '__main__':
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    main()
