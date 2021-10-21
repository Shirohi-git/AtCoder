def main():
    ans = B // C * C
    return print(ans if ans >= A else -1)


if __name__ == '__main__':
    A, B, C = map(int, input().split())

    main()
