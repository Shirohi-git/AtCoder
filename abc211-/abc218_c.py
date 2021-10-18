def main():
    
    def check(Tn):
        tx, ty = divmod(''.join(Tn).index('#'), N)
        dx, dy = tx-sx, ty-sy
        for i, ti in enumerate(Tn):
            for j, tij in enumerate(ti):
                if (tij == '.'):
                    continue
                if (0 <= i-dx < N) and (0 <= j-dy < N):
                    if (S[i-dx][j-dy] == '#'):
                        continue
                return False
        return True

    scnt, tcnt = map(lambda x: sum(xi.count('#') for xi in x), [S, T])
    if scnt != tcnt:
        return print('No')

    sx, sy = divmod(''.join(S).index('#'), N)
    Trev = [''.join(T[i][j] for i in range(N)) for j in range(N)[::-1]]
    ans = check(T) | check([ti[::-1] for ti in T[::-1]])
    ans |= check(Trev) | check([ti[::-1] for ti in Trev[::-1]])
    return print('Yes' if ans else 'No')


if __name__ == '__main__':
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]

    main()
