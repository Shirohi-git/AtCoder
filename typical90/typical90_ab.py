def main():
    imos = [[0] * L for _ in range(L)]
    for pi in PAPER:
        imos[pi[0]][pi[1]] += 1
        imos[pi[2]][pi[3]] += 1
        imos[pi[0]][pi[3]] -= 1
        imos[pi[2]][pi[1]] -= 1

    for i in range(1, L):
        for j in range(L):
            imos[i][j] += imos[i - 1][j]
    for i in range(L):
        for j in range(1, L):
            imos[i][j] += imos[i][j - 1]

    ans = [0] * (N + 1)
    for xi in imos:
        for xij in xi:
            ans[xij] += 1
    return print(*ans[1:], sep='\n')


if __name__ == '__main__':
    N, L = int(input()), 1001
    PAPER = [list(map(int, input().split())) for _ in range(N)]

    main()
