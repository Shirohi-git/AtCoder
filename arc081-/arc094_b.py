def main():
    for a, b in AB:
        ab = a * b
        c = int(ab ** 0.5) - 1
        while (c+1) * (c+2) < ab:
            c += 1
        ans = 2 * c + ((c+1)**2 < ab)
        print(ans - (a != b))
    return


if __name__ == '__main__':
    Q = int(input())
    AB = [list(map(int, input().split())) for _ in range(Q)]

    main()
