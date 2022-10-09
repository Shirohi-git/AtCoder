def main():
    flag = [[0] * N for _ in range(N)]
    for xk in X:
        for i, xi in enumerate(xk):
            for xj in xk[:i]:
                flag[xi-1][xj-1] = flag[xj-1][xi-1] = 1
    res = all(sum(fi) == N-1 for fi in flag)
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    N, M = map(int, input().split())
    X = [list(map(int, input().split()))[1:] for _ in range(M)]

    main()
