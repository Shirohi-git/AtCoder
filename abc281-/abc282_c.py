def main():
    res = []
    cnt = 1
    for si in S:
        res.append('.' if cnt and si == ',' else si)
        cnt ^= (si == '"')
    return print(*res, sep='')


if __name__ == '__main__':
    N = int(input())
    S = input()

    main()
