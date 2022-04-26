def main():

    def calc(a, b, c):
        time, res = 0, 0
        while time < X:
            if time + a > X:
                res += b * (X-time)
                time = X
            else:
                res += a * b
                time += a+c
        return res

    tkhs, aoki = calc(A, B, C), calc(D, E, F)
    ans = ("Takahashi" if tkhs >= aoki else "Aoki")
    return print("Draw" if tkhs == aoki else ans)


if __name__ == '__main__':
    A, B, C, D, E, F, X = map(int, input().split())

    main()
