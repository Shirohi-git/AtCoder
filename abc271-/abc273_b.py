def main():
    ans = X
    for _ in range(K):
        ans, mod = divmod(ans, 10)
        if mod > 4:
            ans += 1
    return print(ans * 10**K)


if __name__ == '__main__':
    X, K = map(int, input().split())

    main()
