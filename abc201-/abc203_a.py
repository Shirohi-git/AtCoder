def main():
    if len({a, b, c}) == 3:
        return print(0)
    return print(a ^ b ^ c)


if __name__ == '__main__':
    a, b, c = map(int, input().split())

    main()
