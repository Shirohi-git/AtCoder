from itertools import accumulate


def main():
    l = min(ai for ai, _ in AB)
    a_mx = max(ai for ai, _ in AB) + 1
    b_mn = min(bi for _, bi in AB)
    ab = [(ai, -bi) for ai, bi in AB]
    ab_sort = sorted(ab + [(M+2, -M-2)])[::-1]

    imos = [0] * (M+2)
    for r in range(a_mx, M+2):
        while r > -ab_sort[-1][1]:
            ab_sort.pop()
            l = min(ab_sort[-1][0], b_mn)
        imos[r-l] += 1
        imos[r] -= 1

    ans = list(accumulate(imos))
    return print(*ans[1:-1])


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    main()
