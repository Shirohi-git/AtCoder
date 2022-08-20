from collections import Counter


def main():
    cnt = Counter(A)
    res = ([*cnt.values()] in [[2, 3], [3, 2]])
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    A = list(map(int, input().split()))

    main()
