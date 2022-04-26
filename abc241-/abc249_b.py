def main():
    res = (len(S) == len(set(S)))
    res &= any(chr(ord('a')+i) in S for i in range(26))
    res &= any(chr(ord('A')+i) in S for i in range(26))
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    S = input()

    main()
