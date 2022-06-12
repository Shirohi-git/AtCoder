def main():        
    mn = []
    for xi, yi in XY:
        res = INF
        for xj, yj in [XY[ai-1] for ai in A]:
            dist2 = (xi-xj)**2 + (yi-yj)**2
            res = min(res, dist2**0.5)
        mn.append(res)
    return print(max(mn))


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(N)]
    INF = 10**9

    main()
