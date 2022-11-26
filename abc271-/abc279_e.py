def main():
    b = [*range(N)]
    pair = []
    for ai in A:
        pair.append((b[ai-1], b[ai]))
        b[ai-1], b[ai] = b[ai], b[ai-1]

    idx = [-1] * N
    for i, bi in enumerate(b):
        idx[bi] = i

    for pi, pj in pair:
        res = 0
        if pi == 0:
            res = pj
        elif pj == 0:
            res = pi
        print(idx[res]+1)
    return


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    main()
