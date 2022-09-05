from math import gcd


def main():
    for d in range(R-L, 0, -1):
        for l in range(L, R+1-d):
            r = l + d
            if gcd(l, r) == 1:
                return print(d)
    return


if __name__ == '__main__':
    L, R = map(int, input().split())

    main()
