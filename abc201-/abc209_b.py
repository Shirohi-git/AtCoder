def main():
    res = sum(A) - N//2
    return print('Yes' if res <= X else 'No')


if __name__ == '__main__':
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    main()
