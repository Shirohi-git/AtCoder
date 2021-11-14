def main():
    from math import gcd

    ans = set()
    for sx, sy in XY:
        for tx, ty in XY:
            dx, dy = sx-tx, sy-ty
            t = gcd(dx, dy)
            if dx != 0 or dy != 0:
                ans.add((dx//t, dy//t))
    return print(len(ans))


if __name__ == '__main__':
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    main()
