def main():
    ans = set(range(10)) - S
    return print(*ans)


if __name__ == '__main__':
    S = set(map(int, input()))

    main()
