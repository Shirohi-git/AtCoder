def main():
    a = [ai-(i % 2) for i, ai in enumerate(A)]
    res = (sum(a) <= X)
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    main()
