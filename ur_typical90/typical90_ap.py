def main():
    if K % 9:
        return print(0)

    dp = [1] + [0] * K
    for i in range(K):
        for j in range(1, 10):
            if i + j > K:
                break
            dp[i + j] += dp[i]
            if dp[i + j] >= MOD1:
                dp[i + j] -= MOD1
    return print(dp[K])


if __name__ == '__main__':
    K = int(input())
    MOD1 = 10**9 + 7

    main()
