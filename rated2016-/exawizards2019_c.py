def main():
    def binary(ok, ng, tgt):
        def is_OK(num, g=tgt):
            idx = num
            for t, d in TD:
                d = (-1 if d == 'L' else 1)
                idx += d * (S[idx] == t)
                if idx in [-1, N]:
                    return (idx == g)
            return False

        while abs(ng - ok) > 1:
            mid = (ok + ng) // 2
            if is_OK(mid):
                ok = mid
            else:
                ng = mid
        return ok

    l = binary(-1, N, -1)
    r = binary(N, -1, N)
    ans = N - (l+1) - (N-r)
    return print(ans)


if __name__ == '__main__':
    N, Q = map(int, input().split())
    S = input()
    TD = [input().split() for _ in range(Q)]

    main()
