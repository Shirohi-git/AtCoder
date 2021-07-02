from math import sin, cos, atan2


def move(a, b, c, d):
    q, r = c[0] - a[0], c[1] - a[1]
    rad = atan2(d[1]-c[1], d[0]-c[0])
    rad -= atan2(b[1]-a[1], b[0]-a[0])
    cd = set(CD)
    for xi, yi in AB:
        xi, yi = xi + q - c[0], yi + r - c[1]
        xm = cos(rad) * xi - sin(rad) * yi + c[0]
        ym = sin(rad) * xi + cos(rad) * yi + c[1]
        xr, yr = round(xm), round(ym)
        if abs(xm-xr) > EPS or abs(ym-yr) > EPS or (xr, yr) not in cd:
            return False
        cd.remove((xr, yr))
    return True


def main():
    def dist(a, b):
        return (a[0]-b[0])**2 + (a[1]-b[1])**2

    if N == 1:
        return print("Yes")

    a, b = AB[0], AB[1]
    for i in range(N):
        for j in range(i+1, N):
            c, d = CD[i], CD[j]
            if dist(a, b) != dist(c, d):
                continue
            if move(a, b, c, d) or move(b, a, c, d):
                return print("Yes")
    return print("No")


if __name__ == '__main__':
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    CD = [tuple(map(int, input().split())) for _ in range(N)]
    EPS = 10**(-6)

    main()
