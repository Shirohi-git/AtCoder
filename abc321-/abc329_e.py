def main():
    t = set()
    for i in range(M):
        for j in range(i+1, M+1):
            tmp = ['#'] * M
            tmp[i:j] = T[i:j]
            t.add(''.join(tmp))

    s = S[::]
    for i in [*range(len(s))] + [*range(len(s))][::-1]:
        if ''.join(s[i:i+M]) in t:
            s[i:i+M] = ['#'] * M

    res = all(si == '#' for si in s)
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    N, M = map(int, input().split())
    S = list(input())
    T = list(input())

    main()
