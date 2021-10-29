def main():
    num = max(A[-1], B[-1])
    dp = [[0] * (num+1) for _ in range(N+1)]
    dp[0] = [1] * (num+1)

    for i, ai, bi in zip(range(1, N+1), A, B):
        for j in range(ai, num+1):
            dp[i][j] += dp[i][j-1] + dp[i-1][j] * (j <= bi)
            dp[i][j] %= MOD9

    return print(dp[-1][B[-1]])


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD9 = 998244353

    main()
