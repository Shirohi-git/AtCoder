def main():
    for si in S:
        print('Yes' if si in T else 'No')
    return


if __name__ == '__main__':
    N, M = map(int, input().split())
    S = input().split()
    T = set(input().split())

    main()
