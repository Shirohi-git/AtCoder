from heapq import heapify, heappop, heappush


def main():
    que = [-ai for ai in A]
    heapify(que)

    ans, aj = 0, min(A)
    while len(que) > 1:
        nxt = -heappop(que) % aj
        if nxt != 0:
            aj = nxt
            heappush(que, -nxt)
        ans += 1
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
