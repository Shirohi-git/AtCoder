def main():
    res = (abs(X - Y) > 1)
    return print("Alice" if res else "Brown")


if __name__ == '__main__':
    X, Y = map(int, input().split())

    main()