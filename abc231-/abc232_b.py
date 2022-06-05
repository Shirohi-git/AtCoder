def main():
    ans = 0
    s_ord = list(map(lambda x: ord(x)-Ord_a, S))
    for j in range(26):
        u = ''.join([chr((si+j)%26 + Ord_a) for si in s_ord])
        ans |= (T == u)
    return print("Yes" if ans else "No")


if __name__ == '__main__':
    S, T = input(), input()
    Ord_a = ord('a')

    main()