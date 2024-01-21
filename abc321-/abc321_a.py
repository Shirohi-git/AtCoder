def main():
    bfo = 10
    flg = True
    for ni in N:
        if bfo <= ni:
            flg = False
        bfo = ni
    print("Yes" if flg else "No")


if __name__ == '__main__':
    N = [*map(int, input())]
    main()
