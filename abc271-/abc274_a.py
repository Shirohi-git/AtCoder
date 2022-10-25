def main():
    if A == B:
        return print('1.000')

    res = 10000*B // A
    if res % 10 > 4:
        res += 10
    return print('0.' + str(res//10).zfill(3))


if __name__ == '__main__':
    A, B = map(int, input().split())

    main()
