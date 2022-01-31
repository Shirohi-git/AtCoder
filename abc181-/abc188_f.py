def main():
    x_len = X.bit_length()
    y = bin(Y)[2:]
    bit_a, bit_b = y[:x_len], y[x_len:]
    int_a, int_a1 = int(bit_a, 2), int(bit_a + bit_b[:1], 2)

    if 0 < X - int_a >= int_a1 - X:
        int_a, bit_b = int_a1, bit_b[1:]

    ans = 0
    solo, cons = 0, 0
    for bi in bit_b[::-1]:
        if bi == '1':
            cons |= solo
            solo = 1 - cons
        elif bi == '0':
            solo, cons = cons, 0
        ans += 1 + solo

    if cons or solo & int_a:
        res = (0 <= int_a - X < 2*X - int_a + 1)
        int_a += 1 - (solo & int_a and res)
    ans += min(abs(int_a - X), abs(2*X - int_a + 1))
    return print(ans)


if __name__ == '__main__':
    X, Y = map(int, input().split())

    main()
