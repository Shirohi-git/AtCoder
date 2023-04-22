def main():
    A[P-1:Q], A[R-1:S] = A[R-1:S], A[P-1:Q]
    return print(*A)


if __name__ == '__main__':
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))

    main()
