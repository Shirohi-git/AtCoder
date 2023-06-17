def main():
    a, b = A, B
    if b < a:
        a, b = b, a
    return print('Yes' if b in [2*a, 2*a+1] else 'No')


if __name__ == '__main__':
    A, B = map(int, input().split())

    main()
