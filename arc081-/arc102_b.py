def main():
    pow2 = [1]
    while pow2[-1] * 4 <= L:
        pow2 += [pow2[-1] * 2]

    n = len(pow2) + 1
    m = []
    for i in range(n-1):
        m.append((i+1, i+2, pow2[i]))
        m.append((i+1, i+2, 0))

    t, l = pow2[-1] * 2, L - pow2[-1] * 2
    while l > 0:
        i = 0
        while (l >> i+1) > 0:
            i += 1
        m.append((i+1, n, t))
        t, l = t + (1 << i), l - (1 << i)

    print(n, len(m))
    for mi in m:
        print(*mi)
    return


if __name__ == '__main__':
    L = int(input())

    main()
