def warshallfloyd(n0, num):
    res = [[(aij if aij > 0 else num) for aij in ai] for ai in A]

    for k in range(n0):
        for i in range(n0):
            for j in range(n0):
                res[i][j] = min(res[i][j], res[i][k] + res[k][j])
    cnt = 0
    for i in range(N):
        cnt += sum(res[i][j] <= P for j in range(i+1, N))
    return cnt


def main():

    def binary(ok, ng, is_left=0):
        def is_OK(num):
            cnt = warshallfloyd(N, num)
            return [cnt > K, cnt >= K][is_left]

        while abs(ng - ok) > 1:
            mid = (ok + ng) // 2
            if is_OK(mid):
                ok = mid
            else:
                ng = mid
        return ok

    max_x, min_x = binary(0, P+2, 1), binary(0, P+2)
    ans = ((max_x - min_x) if max_x <= P else INF)
    return print(0 if min_x > P else ans)


if __name__ == '__main__':
    N, P, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    INF = "Infinity"

    main()
