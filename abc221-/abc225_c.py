def main():
    i, sj = divmod(B[0][0]-1, 7)
    for bi in B:
        j = sj
        for bij in bi:
            if (bij != 7 * i + j + 1) or j > 6:
                return print('No')
            j += 1
        i += 1
    return print('Yes')


if __name__ == '__main__':
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]

    main()
