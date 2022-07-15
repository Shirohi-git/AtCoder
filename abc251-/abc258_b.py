def main():
    num = []
    for i in range(N):
        num += [A[i]*2, A[i][::-1]*2]
        for dx, dy in NEAR:
            res = [A[(j*dx) % N][(i+j*dy) % N] for j in range(N)]
            num += [res*2, res[::-1]*2]

    ans = 0
    for ni in num:
        res = max(int(''.join(ni[j:j+N])) for j in range(N))
        ans = max(ans, res)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [list(input()) for _ in range(N)]
    NEAR = [(1, 0), (0, 1), (1, 1), (1, -1)]

    main()
