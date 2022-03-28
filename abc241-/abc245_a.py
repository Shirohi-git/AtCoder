def main():
    ans = "Takahashi"
    if A > C or (A == C and B > D):
        ans = "Aoki"
    return print(ans)


if __name__ == '__main__':
    A, B, C, D = map(int, input().split())

    main()
