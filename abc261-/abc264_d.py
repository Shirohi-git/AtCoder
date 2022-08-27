def main():
    s = S[:]
    for ti, ni in zip(T[0], T[1]):
        s = s.replace(ti, ni)
    s = [*map(int, s)]

    ans = 0
    for i in range(7):
        for j in range(i):
            ans += s[j] > s[i]
    return print(ans)


if __name__ == '__main__':
    S = input()
    T = "atcoder", "0123456"

    main()
