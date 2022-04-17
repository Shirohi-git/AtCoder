from collections import defaultdict
from bisect import bisect


def main():
    cnt = defaultdict(lambda: [-1])
    for i, ai in enumerate(A):
        cnt[ai].append(i+1)

    for l, r, x in Query:
        resl = bisect(cnt[x], l)
        resr = bisect(cnt[x], r)
        res = resr - resl + (cnt[x][resl-1] == l)
        print(res)
    return


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]

    main()
