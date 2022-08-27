def main():
    def is_CCW(ax, ay, bx, by, cx=0, cy=0):
        res = (bx-cx) * (ay-cy) - (by-cy) * (ax-cx)
        return res < 0
    
    res = 1
    for x,y,z in zip(XY,XY[1:],XY[2:]):
        res &= is_CCW(*x,*y,*z)
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    XY = [list(map(int, input().split())) for _ in range(4)] * 2

    main()
