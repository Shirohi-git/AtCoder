def main():
    x = X

    lst = []
    for si in S:
        if si == 'U':
            if x == 1:
                x = lst.pop()
            x //= 2
        else:
            x = 2*x + (si == 'R')
        if x > MAX:
            lst.append(x)
            x = 1
    return print(x)


if __name__ == '__main__':
    N, X = map(int, input().split())
    S = input()
    MAX = 10**18

    main()
