def main():
    res = (A <= B <= 6*A)
    return print("Yes" if res else "No")


if __name__ == '__main__':
    A, B = map(int, input().split())

    main()
