def main():
    dp = [[C] * G for _ in range(G)]
    dp[0][0] = 0
    for a, b, c in ABC:
        for i in range(a, G)[::-1]:
            for j in range(b, G)[::-1]:
                dp[i][j] = min(dp[i][j], dp[i-a][j-b] + c)
    ans, ma, mb = C, Ma, Mb
    while max(ma, mb) < G:
        ans = min(ans, dp[ma][mb])
        ma, mb = ma+Ma, mb+Mb
    return print(ans if ans < C else -1)

if __name__ == '__main__':
    N, Ma, Mb = map(int, input().split())
    ABC = [map(int, input().split()) for _ in range(N)]
    G, C = 401, 4001

    main()
