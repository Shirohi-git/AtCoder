def main():
    dp = [0] * (N+1)
    for i in range(N):
        for aj in A:
            if aj+i <= N:
                dp[aj+i] = max(dp[aj+i], aj+i - dp[i])
    return print(dp[N])


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    main()