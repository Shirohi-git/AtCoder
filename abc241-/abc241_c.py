def is_connect(x, y):
    
    def is_black(p, q):
        if not (0 <= p < N and 0 <= q < N):
            return -INF
        return (S[p][q] == '#')

    res = [0, 0, 0, 0]
    for i in range(6):
        res[0] += is_black(x+i, y)
        res[1] += is_black(x, y+i)
        res[2] += is_black(x+i, y+i)
        res[3] += is_black(x+i, y-i)
    return max(res)


def main():
    res = 0
    for x in range(N):
        for y in range(N):
            res |= (is_connect(x, y) >= 4)
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    N = int(input())
    S = [input() for _ in range(N)]
    INF = 6

    main()
