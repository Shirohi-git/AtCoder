from itertools import product


def main():
    ans = 0
    for a11, a12, a21, a22 in product(range(1, max(HW)), repeat=4):
        a13, a23 = H1 - a11 - a12, H2 - a21 - a22
        a31, a32 = W1 - a11 - a21, W2 - a12 - a22
        a33 = H3 - a31 - a32
        a33 = (a33 == W3 - a13 - a23) & (a33 > 0)
        if all(m > 0 for m in [a13, a23, a31, a32, a33]):
            ans += 1
    return print(ans)


if __name__ == '__main__':
    H1, H2, H3, W1, W2, W3 = HW = list(map(int, input().split()))

    main()
