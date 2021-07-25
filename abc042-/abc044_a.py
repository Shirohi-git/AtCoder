def main():
    ans = min(K, N) * X
    ans += max(0, N-K) * Y
    return print(ans)


if __name__ == '__main__':
    N, K, X, Y = [int(input()) for _ in range(4)]

    main()