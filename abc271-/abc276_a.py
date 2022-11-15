def main():
    ans = -1
    for i, si in enumerate(S, 1):
        if si == 'a':
            ans = i
    return print(ans)


if __name__ == '__main__':
    S = input()

    main()
