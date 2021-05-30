from math import atan2, pi as PI
from bisect import bisect_right


def rad_to_deg(rad):
    return (((rad) / 2 / PI) * 360)


def main():
    ans = 180
    for a in XY:
        deg = []
        for b in XY:
            if a == b:
                continue
            p, q = b[0] - a[0], b[1] - a[1]
            res = rad_to_deg(atan2(q, p))
            deg.append(res + 360 * (res < 0))
        deg = [max(deg) - 360] + sorted(deg) + [min(deg) + 360]

        for dj in deg[1:N+1]:
            tmp = dj + 180 - 360 * (dj >= 180)
            idx = bisect_right(deg, tmp)
            ans = min(ans, tmp - deg[idx-1], deg[idx] - tmp)
    print(180 - ans)
    return None


if __name__ == '__main__':
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    main()
