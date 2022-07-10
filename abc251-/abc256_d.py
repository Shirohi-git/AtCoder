from itertools import accumulate


def main():
    imos = [0] * INF
    for l, r in LR:
        imos[l] += 1
        imos[r] -= 1
    imos = [*accumulate(imos)]

    ans = []
    lft = 0
    for i in range(INF):
        if (not lft) and imos[i]:
            lft = i
        elif lft and (not imos[i]):
            ans.append((lft, i))
            lft = 0
    for ai in ans:
        print(*ai)
    return


if __name__ == '__main__':
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    INF = 2 * 10**5 + 2

    main()
