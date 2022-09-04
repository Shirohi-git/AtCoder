def main():
    dp = [0] + [-INF] * N
    for ai in A:
        nxt = [0] + [-INF] * N
        for i in range(1, N+1):
            nxt[i] = max(dp[i], dp[i-1] + i * ai)
        dp = nxt
    return print(dp[M])


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    INF = 10**30

    main()
