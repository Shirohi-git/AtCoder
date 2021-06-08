from heapq import heappush, heappop, heapify


def prim(n0):
    flag = [0] * n0
    flag[0] = 1
    que = [(c, j) for j, c in NEAR[0]]
    heapify(que)

    res = 0
    while que:
        c_pq, q = heappop(que)
        if flag[q]:
            continue
        flag[q] = 1
        res += c_pq
        for r, c_qr in NEAR[q]:
            if 1 - flag[r]:
                heappush(que, (c_qr, r))
    return res


def make_edge(p, q):
    (px, py, id1), (qx, qy, id2) = p, q
    cx = min(abs(px - qx), abs(py - qy))
    NEAR[id1].add((id2, cx)), NEAR[id2].add((id1, cx))
    return


def main():
    x_sort = sorted((xi, yi, i) for i, (xi, yi) in enumerate(XY))
    y_sort = sorted((yi, xi, i) for i, (xi, yi) in enumerate(XY))

    for i in range(1, N):
        make_edge(x_sort[i-1], x_sort[i])
        make_edge(y_sort[i-1], y_sort[i])
    ans = prim(N)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    NEAR = [set() for _ in range(N)]
    main()
