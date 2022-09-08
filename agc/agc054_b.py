def main():
    sum_w = sum(W)
    if sum_w % 2:
        return print(0)
    n_max, w_max = N//2+1, sum_w//2+1

    dp = [[0] * n_max for _ in range(w_max)]
    dp[0][0] = 1
    for wi in W:
        for wj in range(wi, w_max)[::-1]:
            for k in range(1, n_max)[::-1]:
                dp[wj][k] += dp[wj-wi][k-1]

    per = [0, 1]
    for i in range(2, N+1):
        per.append(per[-1] * i % MOD9)

    ans = 0
    for i, ci in enumerate(dp[-1]):
        res = per[i] * per[N-i] % MOD9
        ci *= 1 + (i*2 != N)
        ans += res * ci % MOD9
    return print(ans % MOD9)


if __name__ == '__main__':
    N = int(input())
    W = list(map(int, input().split()))
    MOD9 = 998244353

    main()
