def main():
    btm = 0
    while btm < len(S) and S[-1-btm] == 'a':
        btm += 1

    top = 0
    while top < len(S) and S[top] == 'a':
        top += 1

    t = 'a' * max(0, btm-top) + S
    res = (t == t[::-1])
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    S = input()

    main()
