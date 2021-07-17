def main():
    ans = min(A, N) * X
    ans += max(0, N-A) * Y
    return print(ans)


if __name__ == '__main__':
    N, A, X, Y = map(int, input().split())

    main()
