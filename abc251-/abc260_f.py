def main():
    def nearlist():
        s_res = [[] for _ in range(S)]
        for a, b in UV:
            s_res[a - 1].append(b - 1)
        return [sorted(sr) for sr in s_res]

    s_near = nearlist()
    res = [[-1] * T for _ in range(T)]
    for a, sk in enumerate(s_near):
        for i, p in enumerate(sk):
            res_p = res[p-S]
            for q in sk[i+1:]:
                if res_p[q-S] > -1:
                    ans = [p+1, q+1, a+1, res_p[q-S]+1]
                    return print(*ans)
                res_p[q-S] = a
    return print(-1)


if __name__ == '__main__':
    S, T, M = map(int, input().split())
    UV = [list(map(int, input().split())) for _ in range(M)]

    main()
