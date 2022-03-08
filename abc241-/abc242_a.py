def main():
    ans = 0
    if X <= A:
        ans = 1
    elif A < X <= B:
        ans = C / (B - A)
    return print(ans)


if __name__ == '__main__':
    A, B, C, X = map(int, input().split())

    main()
