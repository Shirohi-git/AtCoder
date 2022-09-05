def main():
    def solve(lst, sft):
        res = []
        num = (1 << sft)
        for ai, ci in lst:
            c = 0
            if (ai >> sft) & 1 == 0:
                c = num - (ai & (num - 1))
            ai, ci = ai+c, ci+c
            if ci <= M:
                res.append((ai, ci))
        res = sorted(res, key=lambda x: x[1])
        if len(res) < K or sum(ci for _, ci in res[:K]) > M:
            return lst
        return res

    a = [(ai, 0) for ai in A]
    for i in range(INF)[::-1]:
        a = solve(a, i)
    ans = (1 << INF) - 1
    for ai in a[:K]:
        ans &= ai[0]
    return print(ans)


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    INF = 31

    main()
