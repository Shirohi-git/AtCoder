def main():
    s = S[::-1]
    ans = []
    for si in s:
        if si in or69:
            idx = or69.index(si)
            si = or69[1-idx]
        ans.append(si)
    return print(*ans, sep='')


if __name__ == '__main__':
    S = input()
    or69 = ['6', '9']

    main()
