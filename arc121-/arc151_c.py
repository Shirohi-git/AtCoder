def main():
    if M == 0:
        res = N % 2
    else:
        res = XY[0][0]-1
        for (bx, by), (nx, ny) in zip(XY, XY[1:]):
            res ^= (bx+1 != nx and by == ny)
        res ^= N-XY[-1][0]
    return print("Takahashi" if res else "Aoki")


if __name__ == '__main__':
    N, M = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(M)]

    main()
