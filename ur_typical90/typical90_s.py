def main():
    dp = [[INF] * (N2+1) for _ in range(N2)]
    for j in range(0, N2+1, 2):
        for l in range(N2):
            r = l + j
            if (l == r):
                dp[l][r] = 0
            elif (r <= N2):
                tmp1 = dp[l + 1][r - 1] + abs(A[l] - A[r - 1])
                tmp2 = min(dp[l][k] + dp[k][r] for k in range(l, r, 2))
                dp[l][r] = min(dp[l][r], tmp1, tmp2)
    print(dp[0][N2])
    return


INF = 10**15
if __name__ == '__main__':
    N2 = int(input()) * 2
    A = list(map(int, input().split()))

    main()
