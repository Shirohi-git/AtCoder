def main():
    res = (S == T[:len(S)])
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    S, T = input(), input()
    main()
