def main():
    x, y = 0, 0
    for i, si in enumerate(S):
        for j in range(W):
            if si[j] == 'o':
                x, y = abs(x-i), abs(y-j)
    return print(x + y)


if __name__ == '__main__':
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    main()
