def main():
    blue, red = A, 0
    for i in range(A+1):
        if red * D >= blue:
            return print(i)
        blue += B
        red += C
    return print(-1)


if __name__ == '__main__':
    A, B, C, D = map(int, input().split())

    main()
