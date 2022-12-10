def main():
    mod = T % sum(A)
    for i, ai in enumerate(A, 1):
        mod -= ai
        if mod <= 0:
            return print(i, ai + mod)
    return


if __name__ == '__main__':
    N, T = map(int, input().split())
    A = list(map(int, input().split()))

    main()
