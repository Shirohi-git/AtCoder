def main():
    res = (C-B == B-A)
    return print("Yes" if res else "No")


if __name__ == '__main__':
    A, B, C = sorted(map(int, input().split()))

    main()
