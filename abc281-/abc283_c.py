def main():
    s = [*S]
    ans = 0
    while s:
        if s[-2:].count('0') == 2:
            s.pop()
        s.pop()
        ans += 1
    return print(ans)


if __name__ == '__main__':
    S = input()[::-1]

    main()
