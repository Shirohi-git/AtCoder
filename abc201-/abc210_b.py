def main():
    idx = S.index('1')
    res = bool(idx % 2 == 0)
    return print("Takahashi" if res else "Aoki")


if __name__ == '__main__':
    N = int(input())
    S = input()

    main()
