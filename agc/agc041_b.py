def main():
    def is_OK(idx):
        vote = (V-P+1) * M
        ai = A[idx]
        if ai > A[-P]:
            return True
        if ai+M < A[-P]:
            return False

        for aj in A[:N-P+1]:
            vote -= min(M, ai+M - aj)
        return vote <= 0

    def binary(ok, ng):
        while abs(ng - ok) > 1:
            mid = (ok + ng) // 2
            if is_OK(mid):
                ok = mid
            else:
                ng = mid
        return ok

    res = binary(N, -1)
    return print(N-res)


if __name__ == '__main__':
    N, M, V, P = map(int, input().split())
    A = sorted(map(int, input().split()))

    main()
