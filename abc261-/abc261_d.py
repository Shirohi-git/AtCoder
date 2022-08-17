def main():
    cy = {ci: yi for ci, yi in CY}
    dp = [0] * (N+1)
    for i, xi in enumerate(X, 1):
        max_dp = max(dp)
        for j in range(1,i+1)[::-1]:
            dp[j] = dp[j-1] + xi
            if j in cy:
                dp[j] += cy[j]
        dp[0] = max_dp
    return print(max(dp))


if __name__ == '__main__':
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    CY = [list(map(int, input().split())) for _ in range(M)]

    main()
