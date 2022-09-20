def main():
    def nearlist(n0):
        res = [[i] for i in range(n0)]
        for a, b in AB:
            res[b - 1].append(a - 1)
            res[a - 1].append(b - 1)
        return res

    near = nearlist(N)
    big = int((2*M)**0.5)
    cnt = [len(ni) > big for ni in near]
    big_near = [[nij for nij in ni if cnt[nij]] for ni in near]

    bfo = [-1 for _ in range(N)]
    now = [1] * N
    for i, (x, y) in enumerate(XY):
        if cnt[x-1]:
            print(now[x-1])
        else:
            idx = max(bfo[v] for v in near[x-1])
            print(1 if idx < 0 else XY[idx][1])
        bfo[x-1] = i
        for v in big_near[x-1]:
            now[v] = y
    return


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    Q = int(input())
    XY = [list(map(int, input().split())) for _ in range(Q)]

    main()
