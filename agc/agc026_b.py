def main():
    from math import gcd

    for a, b, c, d in A:
        g = gcd(b, d)
        res = (a < b or d < b or b-g + a % g > c)
        print("Yes" if 1-res else "No")
    return


if __name__ == '__main__':
    T = int(input())
    A = [map(int, input().split()) for _ in range(T)]

    main()
