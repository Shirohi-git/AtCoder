def main():
    dp = [INF] * N
    dp[0] = 0
    for a, b, c in map(lambda x: ABC[x-1], E):
        dp[b-1] = min(dp[b-1], dp[a-1] + c)
    return print(dp[-1] if dp[-1] < INF else -1)


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(M)]
    E = list(map(int, input().split()))
    INF = 10**20

    main()
