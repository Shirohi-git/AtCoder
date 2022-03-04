def main():
    ans = 0
    if min(N, M) == 1:
        ans += pow(K, N*M, MOD9)
        return print(ans)

    for i in range(1, K+1):
        a_cnt = pow(i, N, MOD9) - pow(i-1, N, MOD9)
        b_cnt = pow(K-i+1, M, MOD9)
        ans += a_cnt * b_cnt
        ans %= MOD9
    return print(ans)


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    MOD9 = 998244353

    main()
