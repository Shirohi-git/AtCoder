def main():
    idx = (A+B == 15) + 2 * (A*B == 15)
    return print('x+*'[idx])


if __name__ == '__main__':
    A, B = map(int, input().split())

    main()
