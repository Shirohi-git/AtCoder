def main():
    if X <= M <= N:
        return print(T)
    ans = T - D * X + D * M
    return print(ans)


if __name__ == '__main__':
    N, M, X, T, D = map(int, input().split())

    main()
