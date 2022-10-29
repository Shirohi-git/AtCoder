def main():
    res = max(H)
    return print(H.index(res)+1)


if __name__ == '__main__':
    N = int(input())
    H = list(map(int, input().split()))

    main()
