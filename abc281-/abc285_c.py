def main():
    ans = 0
    for si in S:
        ans *= 26
        ans += ord(si) - ord0
    return print(ans)


if __name__ == '__main__':
    S = input()
    ord0 = ord('A') - 1

    main()
