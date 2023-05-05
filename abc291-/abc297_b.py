def main():
    b, r, k = [], [], []
    for i, si in enumerate(S):
        if si == 'B':
            b.append(i)
        if si == 'K':
            k.append(i)
        if si == 'R':
            r.append(i)

    res = True
    res &= ((b[0]+b[1]) % 2 == 1)
    res &= (r[0] < k[0] < r[1])
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    S = input()

    main()
