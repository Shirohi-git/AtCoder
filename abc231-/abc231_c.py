def main():
    from bisect import bisect_left as bisect

    a = sorted(A)
    for xi in X:
        print(N - bisect(a, xi))
    return


if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]

    main()
