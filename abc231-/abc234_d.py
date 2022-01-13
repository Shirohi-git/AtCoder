def main():
    from heapq import heapify, heappushpop

    que = P[:K]
    heapify(que)
    print(que[0])

    for pi in P[K:]:
        if pi > que[0]:
            heappushpop(que, pi)
        print(que[0])
    return


if __name__ == '__main__':
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    main()
