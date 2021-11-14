def main():

    def binary(ok, ng):
        def is_OK(m):
            cnt = sum(min(ai, m) for ai in A)
            return cnt >= m * K

        while abs(ng - ok) > 1:
            mid = (ok + ng) // 2
            if is_OK(mid):
                ok = mid
            else:
                ng = mid
        return ok

    ans = binary(1, 10**18)
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    main()
