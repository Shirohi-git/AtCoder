from math import gcd


def main():
    ans = (A * B) // gcd(A, B)
    print(ans if ans <= 10**18 else "Large")


if __name__ == '__main__':
    A, B = map(int, input().split())

    main()
