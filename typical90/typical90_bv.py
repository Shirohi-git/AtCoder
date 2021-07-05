def main():
    ans = sum(pow(2, i) * (S_ord[i] - A_ord) for i in range(N))
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    S_ord = list(map(ord, input()))
    A_ord = ord('a')

    main()
