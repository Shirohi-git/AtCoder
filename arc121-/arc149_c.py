def main():
    ans = [[[5, 9, 1],
            [3, 7, 8],
            [6, 2, 4]],
           [[ 9, 11, 13, 15],
            [ 1,  3,  5,  7],
            [ 8,  6,  4,  2],
            [16, 14, 12, 10]],
           [[15, 17, 19, 21, 23],
            [25,  5,  9,  1, 11],
            [13,  3,  7,  8, 14],
            [12,  6,  2,  4, 10],
            [16, 18, 20, 22, 24]]]

    if N < 6:
        for ai in ans[N-3]:
            print(*ai)
        return

    lst = [[], [], [], []]
    for i in range(1, N**2+1):
        idx = (i % 2 == 0) + 2*(i % 3 == 0)
        lst[idx].append(i)

    ans = lst[0] + lst[2] + lst[3] + lst[1]
    for i in range(N):
        print(*ans[N*i:N*i+N])
    return


if __name__ == '__main__':
    N = int(input())

    main()
