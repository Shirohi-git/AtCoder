def main():
    s = S.replace('A', 'BB')
    s = s.replace('BB', 'A')
    return print(s)


if __name__ == '__main__':
    N = int(input())
    S = input()

    main()
