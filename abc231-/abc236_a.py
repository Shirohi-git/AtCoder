def main():
    s = S[::]
    s[A-1], s[B-1] = s[B-1], s[A-1]
    return print(*s, sep='')


if __name__ == '__main__':
    S = list(input())
    A, B = map(int, input().split())

    main()
