from heapq import heappop, heappush
from collections import deque


def main():
    a, a2 = [], deque([])
    for q in Query:
        if len(q) == 2:
            a2.append(q[1])
        if q[0] == 2:
            print(heappop(a) if a else a2.popleft())
        if q[0] == 3:
            for i in a2:
                heappush(a, i)
            a2 = deque([])
    return


if __name__ == '__main__':
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]

    main()
