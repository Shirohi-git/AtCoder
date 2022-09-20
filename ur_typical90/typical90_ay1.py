from itertools import product
from bisect import bisect


def cost_lst(lst):
    res = [[] for _ in range(N+1)]
    for bit in product([0, 1], repeat=len(lst)):
        cost, cnt = 0, 0
        for ai, bi in zip(lst, bit):
            cnt += bi
            cost += ai*bi
        res[cnt].append(cost)
    return [sorted(ri) for ri in res]


def main():
    a1, a2 = A[:N//2], A[N//2:]
    lst1, lst2 = cost_lst(a1), cost_lst(a2)

    ans = 0
    for i in range(N+1):
        if (K-i >= 0):
            ans += sum(bisect(lst2[K-i], P - y1) for y1 in lst1[i])
    return print(ans)


if __name__ == '__main__':
    N, K, P = map(int, input().split())
    A = list(map(int, input().split()))

    main()
