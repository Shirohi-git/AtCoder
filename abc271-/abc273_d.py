from bisect import bisect_left
from collections import defaultdict


def main():
    wall_x = defaultdict(lambda: [-1, W])
    wall_y = defaultdict(lambda: [-1, H])
    for xi, yi in XY:
        wall_x[xi-1].append(yi-1)
        wall_y[yi-1].append(xi-1)
    for xi in wall_x:
        wall_x[xi] = sorted(wall_x[xi])
    for yi in wall_y:
        wall_y[yi] = sorted(wall_y[yi])

    x, y = SX-1, SY-1
    for d, l in DL:
        l, w, z = int(l), wall_x[x], y
        if d in 'UD':
            w, z = wall_y[y], x
        idx = bisect_left(w, z)

        if d == 'L':
            y = max(y-l, w[idx-1] + 1)
        if d == 'R':
            y = min(y+l, w[idx] - 1)
        if d == 'U':
            x = max(x-l, w[idx-1] + 1)
        if d == 'D':
            x = min(x+l, w[idx] - 1)
        print(x+1, y+1)
    return


if __name__ == '__main__':
    H, W, SX, SY = map(int, input().split())
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    DL = [list(input().split()) for _ in range(Q)]

    main()
