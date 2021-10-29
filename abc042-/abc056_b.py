def main():
    ans = abs(a-b) - W
    return print(0 if abs(a-b) <= W else ans)


if __name__ == '__main__':
    W, a, b = map(int, input().split())

    main()
