def main():
    res = sum(si != ti for si, ti in zip(S, T))
    return print('Yes' if res != 2 else 'No')


if __name__ == '__main__':
    S = ''.join(input().split())
    T = ''.join(input().split())

    main()
