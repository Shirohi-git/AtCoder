def main():
    dp = [0] * Tmax
    for ai, bi in sorted(AB):
        for t in range(T)[::-1]:
            dp[t+ai] = max(dp[t]+bi, dp[t+ai])
    return print(max(dp))


if __name__ == '__main__':
    N, T = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    Tmax = 6000

    main()
