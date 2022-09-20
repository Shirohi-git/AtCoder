def main():
    pp, pm, mp, mm = [-1e10]*4
    for x, y in XY:
        pp, pm = max(pp, x + y), max(pm, x - y)
        mp, mm = max(mp, -x + y), max(mm, -x - y)
    for i in QUERY:
        x, y = XY[i]
        ans = max(pp - x - y, pm - x + y, mp + x - y, mm + x + y)
        print(ans)
    return


if __name__ == '__main__':
    N, Q = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(N)]
    QUERY = [int(input())-1 for _ in range(Q)]

    main()
