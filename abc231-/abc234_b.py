def main():
    ans = 0
    for a, b in XY:
        tmp = max((x-a)**2 + (y-b)**2 for x, y in XY)
        ans = max(ans, tmp)
    return print(ans**0.5)


if __name__ == '__main__':
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    main()
