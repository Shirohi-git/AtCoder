def main():
    ans = 0
    a, b = A, B
    while a != b:
        if a < b:
            a, b = b, a
        cnt = (a//b) - (a % b == 0)
        ans += cnt
        a -= cnt * b
    return print(ans)


if __name__ == '__main__':
    A, B = map(int, input().split())

    main()
