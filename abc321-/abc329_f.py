def main():
    itob = [*range(N)]
    box = [set([ci]) for ci in C]
    for ai, bi in Query:
        ai, bi = ai-1, bi-1
        ba, bb = itob[ai], itob[bi]
        if len(box[itob[ai]]) > len(box[itob[bi]]):
            itob[ai], itob[bi] = itob[bi], itob[ai]
            ba, bb = bb, ba
        for aij in box[ba]:
            box[bb].add(aij)
        box[ba] = set()
        print(len(box[itob[bi]]))
    return


if __name__ == '__main__':
    N, Q = map(int, input().split())
    C = list(map(int, input().split()))
    Query = [list(map(int, input().split())) for _ in range(Q)]

    main()
