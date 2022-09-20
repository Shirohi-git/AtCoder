from itertools import combinations_with_replacement as cmb_multi


def main():
    ans = (B <= N and '0' in str(B))
    for r in range(11):
        for cmb in cmb_multi(range(1, 10), r + 1):
            num = 1
            for ci in cmb:
                num *= ci
            b_lst = sorted(map(int, str(B + num)))
            ans += (B + num <= N and list(cmb) == b_lst)
    return print(ans)


if __name__ == '__main__':
    N, B = map(int, input().split())
    main()
