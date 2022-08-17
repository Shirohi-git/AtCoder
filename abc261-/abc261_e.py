def main():
    x = C
    bit = [0, MAX]
    for t, a in TA:
        if t == 1:
            bit = [b & a for b in bit]
        elif t == 2:
            bit = [b | a for b in bit]
        elif t == 3:
            bit = [b ^ a for b in bit]
        x = (x & bit[1]) | ((x ^ MAX) & bit[0])
        print(x)
    return


if __name__ == '__main__':
    N, C = map(int, input().split())
    TA = [list(map(int, input().split())) for _ in range(N)]
    MAX = (1 << 30) - 1

    main()
