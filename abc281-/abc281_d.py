def main():
    dp = [[-1] * D for _ in range(K+1)]
    dp[0][0] = 0
    for ai in A:
        for k in range(K, 0, -1):
            for d_bfo in range(D):
                d = (d_bfo + ai) % D
                if dp[k-1][d_bfo] != -1:
                    dp[k][d] = max(dp[k][d], dp[k-1][d_bfo] + ai)
    return print(dp[K][0])


if __name__ == '__main__':
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))

    main()
