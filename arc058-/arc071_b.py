def main():
    x_cnt = sum((2*i - N + 1) * X[i] for i in range(N))
    y_cnt = sum((2*i - M + 1) * Y[i] for i in range(M))
    return print(x_cnt * y_cnt % MOD1)


if __name__ == '__main__':
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    MOD1 = 10**9 + 7

    main()
