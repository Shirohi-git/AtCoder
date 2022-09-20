def main():
    dp = [[0] * (S+2) for _ in range(N+1)]
    dp[0][0] = 1
    for i, (a, b) in enumerate(AB):
        for j in range(S):
            dp[i + 1][min(S + 1, j + a)] |= dp[i][j]
            dp[i + 1][min(S + 1, j + b)] |= dp[i][j]

    if not dp[N][S]:
        return print("Impossible")

    now = S
    ans = []
    for i, (a, b) in enumerate(AB[::-1]):
        i = N - i
        if now >= a and dp[i-1][now-a]:
            now -= a
            ans.append('A')
        elif now >= b and dp[i-1][now-b]:
            now -= b
            ans.append('B')
    return print(*ans[::-1], sep='')


if __name__ == '__main__':
    N, S = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    main()
