def main():
    x, y = 0, 0
    for xi, yi in XY:
        x, y = x ^ xi, y ^ yi
    return print(x, y)


if __name__ == '__main__':
    XY = [list(map(int, input().split())) for _ in range(3)]

    main()
