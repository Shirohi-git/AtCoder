def main():
    MAX = max(max(a, b) for a, b in AB)

    hw = [[0] * (MAX+1) for _ in range(MAX+1)]
    for a, b in AB:
        hw[a][b] += 1

    acc = [hwi[:] for hwi in hw]
    for i in range(MAX+1):
        for j in range(1, MAX+1):
            acc[i][j] += acc[i][j-1]
    for i in range(1, MAX+1):
        for j in range(MAX+1):
            acc[i][j] += acc[i-1][j]

    ans = 0
    for i in range(1, MAX+1):
        for j in range(1, MAX+1):
            x, y = min(MAX, i+K), min(MAX, j+K)
            cnt = acc[x][y] + acc[i-1][j-1]
            cnt += -acc[x][j-1] - acc[i-1][y]
            ans = max(ans, cnt)
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    main()
