def main():
    x = sorted(XY)[N//2][0]
    y = sorted(XY, key=lambda x: [x[1]])[N//2][1]
    ans = 0
    for xi, yi in XY:
        ans += abs(x-xi) + abs(y-yi)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    main()
