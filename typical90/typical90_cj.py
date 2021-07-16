def nearlist(n0):
    res = [set() for _ in range(n0)]
    for a, b in XY:
        res[a - 1].add(b - 1)
        res[b - 1].add(a - 1)
    for i in range(n0):
        res[i].add(i)
    return res


def main():
    def m_print(id):
        print(len(dp[id]))
        print(*[di+1 for di in sorted(dp[id])])
        print(len(dp2[id]))
        print(*[di+1 for di in sorted(dp2[id])])
        return
    
    idx = sorted(range(N), key=lambda x:A[x])
    sum_a = sum(A)
    near = nearlist(N)
    
    dp = [set() for _ in range(sum_a+1)]
    dp2 = [set() for _ in range(sum_a+1)]
    for i in idx:
        ai = A[i]
        for j in range(sum_a-ai+1):
            if (not (j == 0 or dp[j])) or (dp[j] & near[i]):
                continue
            if dp[j+ai]:
                dp2[j+ai] = (dp[j] | {i})
                return m_print(j+ai)
            dp[j+ai] = (dp[j] | {i})
    return 


if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(Q)]

    main()
