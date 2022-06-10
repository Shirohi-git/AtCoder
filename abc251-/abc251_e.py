def main():

    def dp(ini):
        res = ini[:]
        for ai in A[1:]:
            res = [res[1], min(res) + ai]
        return res

    ans = min(dp([0, INF])[1:] + dp([INF, A[0]]))
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    INF = 10**15

    main()
