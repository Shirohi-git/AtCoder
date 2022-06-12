from itertools import accumulate
from bisect import bisect_right


def main():
    ans, acc = [], [*accumulate([0] + A)]
    for xi in X:
        idx = bisect_right(A, xi)
        res = xi*idx - acc[idx]
        res += acc[-1]-acc[idx] - xi*(N-idx)
        ans.append(res)
    return print(*ans, sep='\n')


if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = sorted(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]

    main()
