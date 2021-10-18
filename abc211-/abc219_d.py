def main():
    dp = [[N+1 for _ in range(Y+1)] for _ in range(X+1)]
    dp[0][0] = 0

    for ai, bi in AB:
        for x in range(X+1)[::-1]:
            for y in range(Y+1)[::-1]:
                nx, ny = min(x+ai, X), min(y+bi, Y)
                dp[nx][ny] = min(dp[nx][ny], dp[x][y]+1)
    return print(dp[X][Y] if dp[X][Y] <= N else -1)


if __name__ == '__main__':
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    main()
