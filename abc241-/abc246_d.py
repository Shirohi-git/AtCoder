def main():
    def calc(x, y):
        return x**3 + x**2*y + x*y**2 + y**3

    ans = INF
    b = 10**6
    for a in range(10**6):
        res = calc(a, b)
        while res >= N and b >= a >= 0:
            ans = min(ans, res)
            b -= 1
            res = calc(a, b)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    INF = 10**18

    main()
