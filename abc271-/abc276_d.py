from math import gcd


def main():
    g = 0
    for ai in A:
        g = gcd(g, ai)

    ans = 0
    for ai in A:
        ai = ai // g
        while ai > 1:
            ans += 1
            if ai % 2 == 0:
                ai //= 2
            elif ai % 3 == 0:
                ai //= 3
            else:
                return print(-1)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
