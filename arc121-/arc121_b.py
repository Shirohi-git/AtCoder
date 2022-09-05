from bisect import bisect


def main():
    rgb = [[-10**16, 10**16] for _ in range(3)]
    for a, c in AC:
        idx = DIC.index(c)
        rgb[idx].append(int(a))
    if sum(len(l) % 2 for l in rgb) == 0:
        return print(0)

    r, g, b = map(sorted, rgb)
    if len(g) % 2 == 0:
        r, g = g[:], r[:]
    if len(b) % 2 == 0:
        r, b = b[:], r[:]

    gb, rg, rb = [10**16], [10**16], [10**16]
    for ri in r[1:-1]:
        idx_g, idx_b = bisect(g, ri), bisect(b, ri)
        rg += [abs(g[idx_g-j] - ri) for j in [0, 1]]
        rb += [abs(b[idx_b-j] - ri) for j in [0, 1]]

    for bi in b[1:-1]:
        idx = bisect(g, bi)
        gb += [abs(g[idx-j] - bi) for j in [0, 1]]
    return print(min(min(gb), min(rg) + min(rb)))


DIC = ['R', 'G', 'B']
if __name__ == '__main__':
    N = int(input())
    AC = [input().split() for _ in range(2 * N)]

    main()
