from math import gcd


def main():
    n = gcd(A, gcd(B, C))
    ans = (A + B + C) // n - 3
    return print(ans)


if __name__ == '__main__':
    A, B, C = map(int, input().split())
    main()
