def main():

    def output(idx):
        while link[idx][0] > 0:
            idx = link[idx][0]

        res = [idx]
        while link[idx][1] > 0:
            idx = link[idx][1]
            res.append(idx)
        return print(len(res), *res, sep=' ')

    link = [[-1, -1] for i in range(N+1)]
    for i, x, y in Query:
        if i == 1:
            link[x][1] = y
            link[y][0] = x
        if i == 2:
            link[x][1] = -1
            link[y][0] = -1
        if i == 3:
            output(x)
    return


if __name__ == '__main__':
    N, Q = map(int, input().split())
    Query = [list(map(int, input().split())) for _ in range(Q)]
    for qi in Query:
        if qi[0] == 3:
            qi.append(0)

    main()
