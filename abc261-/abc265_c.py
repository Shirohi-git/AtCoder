def main():
    def nxt(x, y):
        dir = G[x][y]
        if dir == 'U' and x != 0:
            return x-1, y
        if dir == 'D' and x != H-1:
            return x+1, y
        if dir == 'L' and y != 0:
            return x, y-1
        if dir == 'R' and y != W-1:
            return x, y+1
        return x, y

    flag = [[0] * W for _ in range(H)]
    x, y = (0, 0)
    while flag[x][y] == 0:
        flag[x][y] = 1
        if (x, y) == nxt(x, y):
            return print(x+1, y+1)
        x, y = nxt(x, y)
    return print(-1)


if __name__ == '__main__':
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]

    main()
