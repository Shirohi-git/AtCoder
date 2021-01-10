from collections import deque


def topological(N):
    ans = -10 ** 10
    incnt = [0] * N
    res = [(a[i], 0) for i in range(n)]
    CHILD = [set() for _ in range(N)]
    for x, y in xy:
        CHILD[x - 1].add(y - 1)
        incnt[y - 1] += 1

    que = deque([(i, res[i]) for i in range(n) if incnt[i] == 0])
    while que:
        q, bfo = que.popleft()
        for i in CHILD[q]:
            if res[i][1] - res[i][0] < bfo[0] - max(bfo[1], a[i]) or res[i][1] == 0:
                res[i] = (bfo[0], max(bfo[1], a[i]))
            if bfo[0] > a[i] and CHILD[i]:
                ans = max(res[i][1] - res[i][0], ans)
                res[i] = (a[i], 0)
            incnt[i] -= 1
            if incnt[i] == 0:
                que.append((i, res[i]))
        if bfo[1] > 0:
            ans = max(bfo[1] - bfo[0], ans)
    return ans

n, m = map(int, input().split())
a = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(m)]

print(topological(n))
