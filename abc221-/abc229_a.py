def main():
    res = (S in [".##.", "#..#"])
    return print('Yes' if 1-res else 'No')


if __name__ == '__main__':
    S = input() + input()

    main()
