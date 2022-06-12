from heapq import heappop, heappush
from collections import Counter


def main():
    cnt = Counter()
    mx, mn = [], []
    for t, x, c in Query:
        if t == 1:
            cnt[x] += 1
            heappush(mx, -x), heappush(mn, x)
        if t == 2:
            cnt[x] -= min(cnt[x], c)
        if t == 3:
            while cnt[-mx[0]] == 0:
                heappop(mx)
            while cnt[mn[0]] == 0:
                heappop(mn)
            print(-mx[0] - mn[0])
    return


if __name__ == '__main__':
    Q = int(input())
    Query = []
    for _ in range(Q):
        Query += [([*map(int, input().split())] + [-1, -1])[:3]]

    main()
