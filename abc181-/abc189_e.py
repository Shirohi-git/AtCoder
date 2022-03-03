def main():
    def calc(x, y, sw):
        if sw:
            x, y = y, x
        x = a*x + b
        y = c*y + d
        return (x, y)

    sort_q = [qi+[i] for i, qi in enumerate(AB+[[M+1]])]
    sort_q = sorted(sort_q)[::-1]
    mq = []
    for i, mi in enumerate(OP+[[3]]):
        while i > sort_q[-1][0]-1:
            mq += [[5, *sort_q[-1][1:]]]
            sort_q.pop()
        mq += [(mi + [0,0])[:3]]

    ans = [0] * Q
    swap, a, b, c, d = 0, 1, 0, 1, 0
    for op, p, id in mq:
        if op == 1:
            a, b, c, d, swap = c, d, -a, -b, 1-swap
        if op == 2:
            a, b, c, d, swap = -c, -d, a, b, 1-swap
        if op == 3:
            a, b = -a, -b + 2*p
        if op == 4:
            c, d = -c, -d + 2*p
        if op == 5:
            ans[id] = calc(*XY[p-1], swap)

    for ai in ans:
        print(*ai)
    return

if __name__ == '__main__':
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    OP = [list(map(int, input().split())) for _ in range(M)]
    Q = int(input())
    AB = [list(map(int, input().split())) for _ in range(Q)]

    main()
    