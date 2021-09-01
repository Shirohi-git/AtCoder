def topological(N, near0):
    from collections import deque

    incnt = [0] * N
    child = [set() for _ in range(N)]
    for a, b in near0:
        child[a - 1].add(b - 1)
        incnt[b - 1] += 1

    tprg = []
    que = deque([i for i, num in enumerate(incnt) if num == 0])
    while que:
        q = que.popleft()
        for i in child[q]:
            incnt[i] -= 1
            if incnt[i] == 0:
                que.append(i)
        tprg.append(q)
    return len(tprg) == N


def main():
    near = set()
    for a in A:
        for ai, aj in zip(a, a[1:]):
            near.add((aj, ai))

    res = topological(N, near)
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(2*M)][1::2]

    main()
