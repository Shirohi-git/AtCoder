from itertools import combinations_with_replacement as cmb_with_rep


def main():
    numlst = list(map(int, str(N)))

    def solve(lst):
        res, eq = 0, 1
        for i, ni in enumerate(numlst, 1):
            if eq == 0:
                break
            sm, eq = 0, 0
            for li in lst:
                sm += (li < ni)
                eq += (li == ni)
            res += sm * max(0, (len(lst) - i))
            if eq > 0:
                lst.remove(ni)
        return res + eq

    ans = 0
    for cmb in cmb_with_rep(range(10), r=len(str(N))):
        num = 1
        for ci in cmb:
            num *= (ci if ci > 0 else 1)
        if num <= K:
            ans += solve(list(cmb))
            print(cmb, solve(list(cmb)))
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())

    main()
