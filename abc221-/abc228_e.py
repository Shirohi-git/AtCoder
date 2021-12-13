def main():
    ans = 0
    if M % MOD9:
        kn = pow(K, N, MOD9-1)
        ans = pow(M, kn, MOD9)
    return print(ans)


if __name__ == '__main__':
    N, K, M = map(int, input().split())
    MOD9 = 998244353

    main()
