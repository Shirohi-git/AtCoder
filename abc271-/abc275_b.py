def main():
    res = A * B % MOD9 * C % MOD9
    res -= D * E % MOD9 * F % MOD9
    return print(res % MOD9)


if __name__ == '__main__':
    A, B, C, D, E, F = map(int, input().split())
    MOD9 = 998244353

    main()
