def is_black(x, y):
    if not (0 <= x < N and 0 <= y < N):
        return -6
    return (S[x][y] == '#')


def main():
    res = 0
    for i in range(N):
        if res:
            continue
        for j in range(N):
            res |= (sum(is_black(i, y) for y in range(j, j+6)) > 3)
            res |= (sum(is_black(x, j) for x in range(i, i+6)) > 3)
            res |= (sum(is_black(x, y)
                    for x, y in zip(range(i, i+6), range(j, j+6))) > 3)
            res |= (sum(is_black(x, y)
                    for x, y in zip(range(i, i+6), range(j, j-6, -1))) > 3)
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    N = int(input())
    S = [input() for _ in range(N)]

    main()
