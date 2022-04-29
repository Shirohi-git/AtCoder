from itertools import accumulate
from bisect import bisect_left, bisect_right


def main():
    def binary(x, ok=INF, ng=-1):

        def is_OK(num):
            lft = bisect_left(A, x-num)
            rht = bisect_right(A, x+num)
            if rht + (rht-lft) >= N - 1:
                return True
            return False

        while abs(ng - ok) > 1:
            mid = (ok + ng) // 2
            if is_OK(mid):
                ok = mid
            else:
                ng = mid
        return ok

    acc = [0] + list(accumulate(A))
    odd = [0] + list(accumulate(A[1::2]))

    ans = []
    for xi in X:
        d = binary(xi)
        l = bisect_left(A, xi-d)
        r = l + (N-l)//2

        res = acc[-1] - acc[r] + odd[l//2]
        ans.append(res)
    return print(*ans, sep='\n')


if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    INF = 10**10
    if N % 2:
        N += 1
        A = [-INF] + A

    main()
