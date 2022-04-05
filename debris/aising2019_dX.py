from itertools import accumulate


def main():
    def binary(x, ok=0, ng=N+1):
        def is_OK(num):
            if num:
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

        res = acc[-1]
        ans.append(res)
    return print(*ans, sep='\n')


if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    if N % 2:
        A = [-10**10] + A

    main()
