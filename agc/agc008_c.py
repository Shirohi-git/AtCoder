def main():
    ans = I + O + J + L
    if 1 - (I % 2 == J % 2 == L % 2):
        ans -= 1
        if I % 2 + J % 2 + L % 2 == 2:
            ans -= (I * J * L == 0)
    return print(ans)


if __name__ == '__main__':
    I, O, _, J, L, *_ = map(int, input().split())

    main()
