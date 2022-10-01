def main():
    dp = {0: ''}
    for ai, bi in AB:
        nxt = {}
        for di in dp:
            nxt[di+ai] = dp[di] + 'H'
            nxt[di+bi] = dp[di] + 'T'
        dp = nxt
    return print('Yes\n' + dp[S] if S in dp else 'No')


if __name__ == '__main__':
    N, S = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    main()
