def main():
    s = list(map(list, S))
    for i in range(H):
        for j in range(W-1):
            if s[i][j:j+2] == ['T', 'T']:
                s[i][j:j+2] = ['P', 'C']
    for si in s:
        print(*si, sep='')
    return


if __name__ == '__main__':
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    main()
