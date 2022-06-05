def main():
    ans = list(S)
    ans[L-1:R] = ans[L-1:R][::-1]
    return print(*ans, sep='')


if __name__ == '__main__':
    L, R = map(int, input().split())
    S = input()

    main()