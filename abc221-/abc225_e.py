def main():
    ans = 0
    rad = []
    for x, y in XY:
        mx = (BigM*y // (x-1)) if x > 1 else (10**30)
        rad.append((mx, BigM*(y-1) // x))

    bfo = 0
    for mx, mn in sorted(rad):
        if mn >= bfo:
            ans += 1
            bfo = mx
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    BigM = 10**20 #(傾きの最小差が1e-20)

    main()
