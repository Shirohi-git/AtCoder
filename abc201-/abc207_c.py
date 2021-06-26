def main():
    tlr = sorted(TLR, key=lambda x: x[1])
    ans = 0
    for i, (ti, _, ri) in enumerate(tlr):
        for tj, lj, _ in tlr[i+1:]:
            if ti in [1, 3] and tj in [1, 2]:
                ans += (ri >= lj)
            else:
                ans += (ri > lj)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    TLR = [list(map(int, input().split())) for _ in range(N)]

    main()
