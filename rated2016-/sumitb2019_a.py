def main():
    res = (M1 != M2)
    return print(1 if res else 0)


if __name__ == '__main__':
    M1, D1 = map(int, input().split())
    M2, D2 = map(int, input().split())

    main()
