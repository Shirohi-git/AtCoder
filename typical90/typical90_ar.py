def main():
    shift = 0
    for t, x, y in Txy:
        xs, ys = (x-1-shift) % N, (y-1-shift) % N
        if t == 1:
            A[xs], A[ys] = A[ys], A[xs]
        if t == 2:
            shift += 1
        if t == 3:
            print(A[xs])
    return


if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    Txy = [list(map(int, input().split())) for _ in range(Q)]

    main()
