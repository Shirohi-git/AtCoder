def main():
    ans = ((Y-X+9) // 10)
    return print(max(ans, 0))


if __name__ == '__main__':
    X, Y = map(int, input().split())

    main()