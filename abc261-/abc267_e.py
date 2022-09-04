from heapq import heapify, heappop, heappush


def main():
    def weighted_nearlist(n0, lst0):
        res = [[] for _ in range(n0)]
        for u, v in lst0:
            res[u-1].append((v-1, A[v-1]))
            res[v-1].append((u-1, A[u-1]))
        return res

    near = weighted_nearlist(N, UV)
    cost = [sum(w for _, w in ni) for ni in near]
    que = [(cost[i], i) for i in range(N)]
    heapify(que)

    flag = [0] * N
    while que:
        _, q = heappop(que)
        if flag[q]:
            continue
        flag[q] = 1
        for i, _ in near[q]:
            if flag[i]:
                continue
            cost[i] -= A[q]
            heappush(que, (cost[i], i))
    return print(max(cost))


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    UV = [list(map(int, input().split())) for _ in range(M)]

    main()
