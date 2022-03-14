from itertools import accumulate


def main():
    acc = list(accumulate(X))
    for i in range(1, len(acc))[::-1]:
        acc[i-1] += acc[i] // 10
        acc[i] %= 10
    return print(*acc, sep='')


if __name__ == '__main__':
    X = list(map(int, input()))

    main()
