def main():
    top, bottom = [], []
    for t, x in TX:
        ts = len(top)
        if t == 1:
            top.append(x)
        if t == 2:
            bottom.append(x)
        if t == 3:
            print(top[ts-x] if x <= ts else bottom[x-ts-1])
    return


if __name__ == '__main__':
    Q = int(input())
    TX = [list(map(int, input().split())) for _ in range(Q)]

    main()
