def main():
    d_idx = 0
    ans = (0, 0)
    for ti in T:
        if ti == 'S':
            ans = tuple(ai+di for ai, di in zip(ans, DIR[d_idx]))
        if ti == 'R':
            d_idx = (d_idx+1) % 4
    return print(*ans)


if __name__ == '__main__':
    N = int(input())
    T = input()
    DIR = [[1, 0], [0, -1], [-1, 0], [0, 1]]

    main()
