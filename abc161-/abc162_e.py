def main():
    ans = 0
    cnt = [0] * (K+1)
    for i in range(1, K+1):
        cmb = pow(K//i, N, MOD1)
        plus = i - cnt[i]
        ans += cmb * plus % MOD1
        for j in range(i, K+1, i):
            cnt[j] += plus
    return print(ans % MOD1)


if __name__ == '__main__':
    N, K = map(int, input().split())
    MOD1 = 10**9 + 7

    main()
    