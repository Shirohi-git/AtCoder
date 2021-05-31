def main():
    return print('Yes' if A < pow(C, B) else 'No')


if __name__ == '__main__':
    A, B, C = map(int, input().split())
    main()
