def main():
    ans = [ai for ai in A if ai % 2 == 0]
    return print(*ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
