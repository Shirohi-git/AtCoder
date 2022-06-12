def main():
    def lcm(X, Y):
        from math import gcd
        return (X * Y) // gcd(X, Y)

    L = lcm(A, B)
    l, a, b = N//L, N//A, N//B
    ans = N * (N+1) // 2
    ans -= A * a*(a+1)//2 + B * b*(b+1)//2
    ans += L * l*(l+1)//2
    return print(ans)


if __name__ == '__main__':
    N, A, B = map(int, input().split())

    main()
