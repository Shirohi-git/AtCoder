from heapq import heappush, heappop


def main():
    que = []
    plus = 0
    for q in Query:
        if q[0] == 1:
            heappush(que, q[1] - plus)
        if q[0] == 2:
            plus += q[1]
        if q[0] == 3:
            print(heappop(que) + plus)
    return


if __name__ == '__main__':
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]

    main()
