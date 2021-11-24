def warshallfloyd(n0, lst0, pre):
    res = pre
    for i in range(n0):
        for j in range(n0):
            d_ij, flag = lst0[i][j], 1
            for k in range(n0):
                if k == i or k == j:
                    continue
                d_ik, d_kj = lst0[i][k], lst0[k][j]
                if d_ij > d_ik + d_kj:
                    return(-1)
                elif d_ij == d_ik + d_kj and flag:
                    res -= d_ij
                    flag = 0
    return res // 2


def main():
    now = sum(sum(ai) for ai in A)
    ans = warshallfloyd(N, A, now)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    main()
