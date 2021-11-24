def arg_sort(points, ymax=10**20):

    def sub_sort(sub_p):
        if (not sub_p) or (sub_p[0][0] == 0):
            return sub_p
        res = sorted(sub_p, key=lambda p: p[1] * ymax // p[0])
        return res

    group = [[], [], [], [], []]
    for xi, yi in points:
        if yi < 0:
            group[2 + (xi >= 0) + (xi > 0)].append((xi, yi))
        elif yi >= 0:
            group[(xi <= 0) + (xi < 0)].append((xi, yi))

    res = sum([sub_sort(gi) for gi in group], [])
    return res


def main():
    def dist(xy):
        return xy[0]**2 + xy[1]**2

    p_sort = arg_sort(XY) * 2
    acc = [(0, 0)]
    for x, y in p_sort:
        p, q = acc[-1]
        acc.append((p+x, q+y))

    ans = (0, 0)
    for i in range(N+1, 2*N + 1):
        for j in range(i-N, i):
            (xi, yi), (xj, yj) = acc[i], acc[j]
            res = ((xi-xj), (yi-yj))
            ans = max([ans, res], key=lambda p: dist(p))
    print(dist(ans)**0.5)


if __name__ == '__main__':
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    main()
