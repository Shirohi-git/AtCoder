def main():
    dp = [(i == A[0]) for i in range(Ten)]

    for ai in A[1:]:
        nxt = [0 for _ in range(Ten)]
        for j in range(Ten):
            nxt[(ai+j) % Ten] += dp[j]
            nxt[(ai*j) % Ten] += dp[j]
        dp = [nj % MOD9 for nj in nxt]
    return print(*dp, sep='\n')


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    MOD9 = 998244353
    Ten = 10

    main()
