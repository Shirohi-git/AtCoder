def main():
    ans = K
    if (N > 1):
        ans *= K - 1
    if (N > 2):
        ans *= pow(K - 2, N - 2, MOD1)
    return print(ans % MOD1)


if __name__ == '__main__':
    N, K = map(int, input().split())
    MOD1 = 10**9 + 7

    main()
