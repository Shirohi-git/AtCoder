def main():

    def win(i, x, xc, y):
        pat = [('P', 'G'), ('C', 'P'), ('G', 'C')]
        res = (A[x][i], A[y][i]) in pat
        cnt.append((xc - res, x))
        return None

    nxt = [(0, i) for i in range(2 * N)]
    for i in range(M):
        cnt = []
        for (uc, u), (vc, v) in zip(nxt[::2], nxt[1::2]):
            win(i, u, uc, v), win(i, v, vc, u)
        nxt = sorted(cnt)
    ans = [idx+1 for _, idx in nxt]
    return print(*ans, sep='\n')


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [input() for _ in range(2 * N)]

    main()
