def main():
    res = (A+1 == B or ((A, B) == (1, 10)))
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    A, B = map(int, input().split())

    main()
