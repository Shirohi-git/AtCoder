def main():
    ans = min(N*X, (N//3)*Y + (N % 3)*X)
    return print(ans)


if __name__ == '__main__':
    X, Y, N = map(int, input().split())

    main()
