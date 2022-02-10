def main():
    res = (-Pow2 <= N < Pow2)
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    N = int(input())
    Pow2 = pow(2, 31)

    main()
