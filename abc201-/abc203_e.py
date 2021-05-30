from collections import defaultdict
from heapq import heappop, heappush
from bisect import bisect_right


def solve(NEAR):
    cnt = set()
    que = [(0, N)]
    flag = defaultdict(lambda: 1)
    while que:
        x, y = heappop(que)
        idx_st = bisect_right(NEAR[y], x)
        nxt_st = 2 * N
        if idx_st < len(NEAR[y]):
            nxt_st = NEAR[y][idx_st]
        elif idx_st == len(NEAR[y]):
            cnt.add(y)

        if y > 0:
            idx = bisect_right(NEAR[y-1], x)
            for nxt_l in NEAR[y-1][idx:]:
                tmp_l = (nxt_l, y-1)
                if nxt_st >= nxt_l and flag[tmp_l]:
                    heappush(que, tmp_l)
                    flag[tmp_l] = 0

        if y < 2 * N:
            idx = bisect_right(NEAR[y+1], x)
            for nxt_r in NEAR[y+1][idx:]:
                tmp_r = (nxt_r, y+1)
                if nxt_st >= nxt_r and flag[tmp_r]:
                    heappush(que, tmp_r)
                    flag[tmp_r] = 0
    return len(cnt)


def main():
    black = defaultdict(list)
    for x, y in sorted(XY):
        black[y].append(x)
    ans = solve(black)
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(M)]
    main()
