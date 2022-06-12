from itertools import accumulate


def main():
    dp = [0] + [1] * M
    for _ in range(N-1):
        dp = [*accumulate(dp)]
        nxt = [0] + [dp[-1]] * M
        for j in range(1, M+1):
            if K > 0:
                nxt[j] += dp[max(0, j-K)] - dp[min(M, j+K-1)]
        dp = [ni % MOD9 for ni in nxt]
    return print(sum(dp) % MOD9)


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    MOD9 = 998244353

    main()
