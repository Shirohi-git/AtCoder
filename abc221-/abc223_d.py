def topological(N, edge0):
    from heapq import heapify, heappop, heappush

    incnt = [0] * N
    child = [[] for _ in range(N)]
    for a, b in edge0:
        child[a - 1].append(b - 1)
        incnt[b - 1] += 1

    tprg = []
    que = [i for i, num in enumerate(incnt) if num == 0]
    heapify(que)
    while que:
        q = heappop(que)
        for i in child[q]:
            incnt[i] -= 1
            if incnt[i] == 0:
                heappush(que, i)
        tprg.append(q+1)
    return tprg


def main():
    ans = topological(N, AB)
    return print(*(ans if len(ans) == N else [-1]))


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    main()