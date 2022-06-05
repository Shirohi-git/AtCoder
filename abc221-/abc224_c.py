def main():
    ans = 0
    for x1, y1 in XY:
        for x2, y2 in XY:
            for x3, y3 in XY:
                ans += ((x1-x3)*(y2-y3) - (x2-x3)*(y1-y3) != 0)
    return print(ans // 6)


if __name__ == '__main__':
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    main()