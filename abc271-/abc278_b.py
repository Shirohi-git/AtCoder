def main():
    def check(h, m):
        res = (0 <= h < 24 and 0 <= m < 60)
        return res

    for m in range(M, 60):
        new_h = H // 10 * 10 + m // 10
        new_m = H % 10 * 10 + m % 10
        if check(new_h, new_m):
            return print(H, m)

    for h in range(H+1, H+24):
        h %= 24
        for m in range(60):
            new_h = h // 10 * 10 + m // 10
            new_m = h % 10 * 10 + m % 10
            if check(new_h, new_m):
                return print(h, m)
    return


if __name__ == '__main__':
    H, M = map(int, input().split())

    main()
